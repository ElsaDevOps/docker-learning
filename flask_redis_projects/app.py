from flask import Flask, jsonify
import redis




app = Flask(__name__)

@app.route('/')
def hello_world():
    
# Connect to the Redis database
    redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def home():
    # Increment a counter in Redis
    count = redis_client.incr('hits')
    return jsonify(message="Welcome to the Flask-Redis app!", hits=count)
  

if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)