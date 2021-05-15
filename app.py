from flask import Flask
from os import getenv

app = Flask(__name__)

def check_env(var, fallback):
        r = getenv(var)
        if r:
                return r
        else:
                return fallback

tier = check_env("TIER", "undefined")

@app.route('/')
def hello_world():
    return tier
