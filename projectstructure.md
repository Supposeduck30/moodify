moodify/
├── app.py                      # Main Flask app
├── requirements.txt            # Dependencies (Flask, Spotipy, OpenAI, etc.)
├── .gitignore
├── README.md
├── .env                        # Environment variables (Spotify & OpenAI keys)
├── templates/
│   ├── index.html              # Homepage with mood input form
│   └── results.html            # Display playlist results
├── static/
│   ├── style.css               # CSS (optional)
│   └── script.js               # JS if needed
├── spotify_utils.py            # Functions to interact with Spotify API
├── ai_utils.py                 # Optional: functions to parse mood using OpenAI
└── .kiro/                      # Hackathon specs & hooks (mandatory)
    ├── specs/
    │   └── moodify-spec.yaml
    └── hooks/
        └── sample-hook.py
