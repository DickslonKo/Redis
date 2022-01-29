from flask import Flask
import redis
import time

app = Flask(__name__)
@app.route("/")
def Hello_World(x):
    r = redis.Redis(
        host='10.170.0.2',
        port=6379,
        db = 0)

    if r.exists(x) == 1:
        return r.get(x)
    else:
        for i in range (1000000):
            result = int(x) + 1
            time.sleep(5)
            r.set(x, result, ex=30)
            return result


