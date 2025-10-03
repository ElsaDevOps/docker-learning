from flask import Flask, jsonify, render_template
import redis
import os



# Flask & Redis

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))

# connect to redis (global variable)
r = redis.Redis(host=redis_host, port=redis_port, db=0)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/count')
def count():
    visits = r.incr('visit_count')
    return render_template("count.html", visits=visits)

                                  


    


if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)