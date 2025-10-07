from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import redis
import json
import os

app = Flask(__name__)
CORS(app) 

redis_host = os.getenv('REDIS_HOST', 'redis')

try:
    r = redis.Redis(host=redis_host, port=6379, db=0, decode_responses=True)
    r.ping()
    print(f"Connected to Redis successfully at host: {redis_host}!")
except redis.exceptions.ConnectionError as e:
    print(f"Could not connect to Redis: {e}")
    r = None

@app.route("/")
def index():
    return jsonify({
        "status": "online",
        "message": "Visitor Analytics API is running.",
        "redis_connected": r is not None
    })

@app.route("/api/visitors", methods=['GET', 'POST'])
def handle_visitors():
    if not r:
        return jsonify({"error": "Database connection failed"}), 500

    if request.method == 'POST':
        data = request.get_json()
        data['created_date'] = datetime.utcnow().isoformat() + 'Z'
        r.lpush('visitors', json.dumps(data))
        r.ltrim('visitors', 0, 999)
        return jsonify({"status": "success", "data": data}), 201

    if request.method == 'GET':
        visitors_str = r.lrange('visitors', 0, -1)
        visitors = [json.loads(v) for v in visitors_str]
        return jsonify(visitors)