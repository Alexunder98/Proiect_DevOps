#!usr/bin/python3

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    sr = "/ProgrammerHUmor"
    url = "https://meme-api.com/gimme" + sr
    # url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

@app.route("/liveness")
def liveness():
    return "Ing DevSchool 2023 project LIVENESS\n"

# Flask is going to run on our host, port 5001
app.run(host="0.0.0.0", port=5001)
