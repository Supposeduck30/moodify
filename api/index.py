from flask import Flask, render_template, request
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dotenv import load_dotenv
from spotify_utils import get_playlist_by_mood

load_dotenv()

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = os.getenv("SECRET_FLASK_KEY", "default_secret")

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        mood = request.form.get("mood")
        playlists = get_playlist_by_mood(mood)
        return render_template("results.html", playlists=playlists)
    
    return render_template('index.html')

# This is required for Vercel
if __name__ == "__main__":
    app.run(debug=True)