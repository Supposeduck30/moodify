from flask import Flask, render_template
from flask import request 
import os 
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key= os.getenv("SECRET_FLASK_KEY", "default_secret")

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

