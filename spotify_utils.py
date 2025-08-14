import spotipy
import os 
from spotipy.oauth2 import SpotifyClientCredentials 
from dotenv import load_dotenv
load_dotenv()

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
))

def get_playlist_by_mood(mood):
    results = spotify.search(q=mood, type='playlist', limit=5)
    playlists= []
    items = results.get('playlists', {}.get('items', []))
    for item in items:
        playlists.append({
            'name': item['name'],
            'url': item['external_urls']['spotify']
        })
    return playlists
