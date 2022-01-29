from flask import Flask
import redis

app = Flask(__name__)
@app.route("/Hello World/")
def Hello_World():
    return("Hello World")

