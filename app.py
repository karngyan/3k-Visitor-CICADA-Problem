from flask import Flask,render_template
import redis


app = Flask(__name__)
# red = redis.Redis("Your VS IP")
red = redis.Redis("localhost")

@app.route('/')
def hello():

    red.incr("count")
    tmp = int(red.get("count"))
    # print(tmp)
    if(tmp%3000 == 0):
        return render_template("flag.html")
    return render_template("noflag.html", count = tmp)

if __name__ == "__main__":
    app.run()