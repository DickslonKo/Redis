from flask import Flask
import redis

app = Flask(__name__)
@app.route("/Hello World/")
def Hello_World():
    #Ask Redis, does x exist?
    #if not exist, return stored value
    #if not exist, calculate
    x = 0
    for i in range (1000000):
        result = x + 1
    return result

