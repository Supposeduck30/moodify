moodify/
├── manage.py
├── moodify/                    # Django project config folder
│   ├── __init__.py
│   ├── settings.py             # Django settings (add Spotify & OpenAI configs here)
│   ├── urls.py                 # Root URL routing
│   ├── asgi.py
│   └── wsgi.py
├── playlist/                   # Django app for playlist logic & views
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py                # Core views (handle mood input, fetch playlists)
│   ├── urls.py                 # App URL routing
│   ├── templates/
│   │   └── playlist/
│   │       ├── index.html      # Homepage with mood input form
│   │       └── results.html    # Show playlist results
│   ├── static/
│   │   └── playlist/
│   │       └── style.css       # CSS styles (optional)
│   └── tests.py
├── .gitignore
├── requirements.txt            # Python dependencies (django, spotipy, openai, etc.)
├── Procfile                   # For Heroku deployment (web: gunicorn moodify.wsgi)
├── README.md
├── .env                       # Environment variables (client IDs, secrets)
└── .kiro/                     # For hackathon specs & hooks (keep this folder)
    ├── specs/
    │   └── moodify-spec.yaml  # Spec file describing project features
    └── hooks/
        └── sample-hook.py     # Optional automation hooks for Kiro  what do i staart with 