# 🎵 Moodify

**Find Spotify playlists that match your vibe**

Moodify is a Flask web application that uses the Spotify Web API to discover playlists based on your current mood. Whether you're feeling happy, sad, energetic, or chill, Moodify helps you find the perfect soundtrack for your moment.

## ✨ Features

- **Mood-based playlist discovery** - Enter any mood and get curated Spotify playlists
- **Interactive emoji picker** - Quick-select popular moods with emoji buttons
- **Clean, responsive UI** - Beautiful interface that works on all devices
- **Direct Spotify integration** - Links directly to playlists on Spotify
- **Artist lookup tools** - Bonus utilities for finding artist information and images

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Spotify Developer Account (for API credentials)

### Running Locally

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd moodify
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your Spotify API credentials:
   ```
   SPOTIPY_CLIENT_ID=your_spotify_client_id
   SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
   SECRET_FLASK_KEY=your_flask_secret_key
   ```

5. **Run the application**
   ```bash
   python api/index.py
   ```

6. **Open your browser** and visit `http://localhost:5000`

## 🔑 Getting Spotify API Credentials

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Log in with your Spotify account
3. Click "Create App"
4. Fill in app details (name, description)
5. Copy your Client ID and Client Secret to your `.env` file

## 🎯 How It Works

1. **Enter your mood** - Type anything like "happy", "workout", "study", or "chill"
2. **Get recommendations** - Moodify searches Spotify for playlists matching your mood
3. **Discover music** - Click any playlist to open it directly in Spotify
4. **Quick picks** - Use emoji buttons for instant mood-based searches

## 📁 Project Structure

```
moodify/
├── api/
│   └── index.py          # Main Flask application (Vercel serverless)
├── spotify_utils.py      # Spotify API integration
├── templates/
│   ├── index.html        # Homepage with mood input
│   └── results.html      # Playlist results page
├── static/
│   ├── style.css         # Styling
│   └── script.js         # Frontend interactions
├── vercel.json           # Vercel deployment configuration
├── requirements.txt      # Python dependencies
└── examples/             # Development utilities (gitignored)
    ├── artistimage.py    # Artist lookup utility
    └── coverart.py       # Album art utility
```

## 🛠️ Tech Stack

- **Backend**: Flask (Python web framework)
- **API**: Spotify Web API via Spotipy
- **Frontend**: HTML, CSS, JavaScript
- **Environment**: python-dotenv for configuration

## 🎨 Example Moods

Try searching for:
- **Emotions**: happy, sad, angry, excited, calm
- **Activities**: workout, study, party, sleep, driving
- **Genres**: jazz, rock, electronic, classical, hip-hop
- **Vibes**: chill, energetic, romantic, nostalgic, upbeat

## 🤝 Contributing

This project was created for a hackathon by **Anish Bommena** and **Krish Joshi**. Feel free to fork and improve!

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

*Made with ❤️ and lots of ☕ during a hackathon*
