import os
from typing import List

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()


app = Flask(__name__)
CORS(app)


client_id = os.getenv("SPOTIFY_CLIENT_ID", "49b3db8fca06433596cbb56b04907043")  
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", "87322957ec4c4250bb44b0778d5d9d66")

if not client_id or not client_secret:
    raise RuntimeError("Missing SPOTIFY_CLIENT_ID / SPOTIFY_CLIENT_SECRET environment variables.")

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
)




def _parse_limit(value: str, default: int = 30, lo: int = 1, hi: int = 100) -> int:
    try:
        return max(lo, min(hi, int(value)))
    except Exception:
        return default


def _split_csv(value: str | None) -> List[str]:
    if not value:
        return []
    return [x.strip() for x in value.split(',') if x.strip()]




@app.get("/")
def health():
    return {"status": "ok", "auth": "client_credentials"}


@app.get("/api/recommendations")
def recommendations():
    """
    Server-side proxy to Spotify's recommendations using app-only (client credentials) auth.

    Query params (any Spotify-supported params are forwarded):
      - seed_artists, seed_tracks, seed_genres (CSV)
      - limit (1..100), market
      - min_*/max_*/target_* audio features (e.g., target_valence, min_tempo)

    Example:
      /api/recommendations?seed_genres=pop,dance&target_valence=0.8&limit=25
    """

    params = {}
    limit = _parse_limit(request.args.get("limit", "30"))
    params["limit"] = limit

    for key in ("seed_artists", "seed_tracks", "seed_genres"):
        csv = request.args.get(key)
        if csv:
            params[key] = _split_csv(csv)

    market = request.args.get("market")
    if market:
        params["market"] = market


    for k, v in request.args.items():
        if k.startswith(("min_", "max_", "target_")):
            try:
                params[k] = float(v) if k != "target_key" and k != "target_mode" and k != "target_time_signature" else int(v)
            except ValueError:
                params[k] = v  # let API reject bad values

    try:
        rec = sp.recommendations(**params)
    except spotipy.SpotifyException as e:
        return jsonify({"error": "spotify_error", "details": str(e)}), 400

    tracks = []
    for t in rec.get("tracks", []):
        album = t.get("album") or {}
        images = album.get("images") or []
        tracks.append({
            "id": t.get("id"),
            "name": t.get("name"),
            "artists": ", ".join(a.get("name") for a in t.get("artists", [])),
            "uri": t.get("uri"),
            "external_url": (t.get("external_urls") or {}).get("spotify"),
            "preview_url": t.get("preview_url"),
            "album": {"name": album.get("name"), "image": (images[0]["url"] if images else None)},
        })

    return jsonify({"count": len(tracks), "tracks": tracks})


@app.get("/api/tracks")
def get_tracks():
    """Batch fetch basic track metadata.
    Query: ids=comma,separated,ids  (up to 50)
    Optional: market=US etc.
    """
    ids = _split_csv(request.args.get("ids"))
    if not ids:
        return jsonify({"error": "missing_ids"}), 400
    market = request.args.get("market")
    try:
        data = sp.tracks(tracks=ids, market=market)
    except spotipy.SpotifyException as e:
        return jsonify({"error": "spotify_error", "details": str(e)}), 400

    out = []
    for t in data.get("tracks", []) or []:
        if not t:
            continue
        album = t.get("album") or {}
        images = album.get("images") or []
        out.append({
            "id": t.get("id"),
            "name": t.get("name"),
            "artists": ", ".join(a.get("name") for a in t.get("artists", [])),
            "duration_ms": t.get("duration_ms"),
            "explicit": t.get("explicit"),
            "popularity": t.get("popularity"),
            "uri": t.get("uri"),
            "external_url": (t.get("external_urls") or {}).get("spotify"),
            "album": {"name": album.get("name"), "image": (images[0]["url"] if images else None)},
        })
    return jsonify({"count": len(out), "tracks": out})


@app.get("/api/audio-features")
def audio_features():
    """Batch fetch audio features for tracks.
    Query: ids=comma,separated,ids  (up to 100)
    """
    ids = _split_csv(request.args.get("ids"))
    if not ids:
        return jsonify({"error": "missing_ids"}), 400
    try:
        feats = sp.audio_features(tracks=ids)
    except spotipy.SpotifyException as e:
        return jsonify({"error": "spotify_error", "details": str(e)}), 400
    return jsonify({"count": len([f for f in feats if f]), "audio_features": feats})


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
