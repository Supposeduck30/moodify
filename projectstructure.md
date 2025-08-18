moodify/
├── api/
│   └── index.py                # Main Flask app (Vercel serverless function)
├── requirements.txt            # Dependencies (Flask, Spotipy, python-dotenv)
├── vercel.json                 # Vercel deployment configuration
├── .gitignore
├── README.md
├── .env                        # Environment variables (Spotify keys & Flask secret)
├── .env.example                # Template for environment variables
├── templates/
│   ├── index.html              # Homepage with mood input form
│   └── results.html            # Display playlist results
├── static/
│   ├── style.css               # CSS styling
│   └── script.js               # Frontend JavaScript
├── spotify_utils.py            # Functions to interact with Spotify API
├── ai_utils.py                 # Optional: functions to parse mood using AI
└── examples/                   # Development examples (gitignored)
    ├── artistimage.py          # Artist lookup utility
    └── coverart.py             # Album art utility
