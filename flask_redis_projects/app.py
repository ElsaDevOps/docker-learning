# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import redis # <-- Import redis
import json  # <-- Import json for serializing data

app = Flask(__name__)
CORS(app) 

# Connect to our Redis container.

try:
    r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)
    r.ping()
    print("Connected to Redis successfully!")
except redis.exceptions.ConnectionError as e:
    print(f"Could not connect to Redis: {e}")
    r = None

@app.route("/api/visitors", methods=['GET', 'POST'])
def handle_visitors():
    if not r:
        return jsonify({"error": "Database connection failed"}), 500

    if request.method == 'POST':
        data = request.get_json()
        data['created_date'] = datetime.utcnow().isoformat() + 'Z'
        
        # Convert the visitor dictionary to a JSON string and push it to the list
        r.lpush('visitors', json.dumps(data))
        
        # Optional: keep the list trimmed to the latest 1000 visitors
        r.ltrim('visitors', 0, 999)

        return jsonify({"status": "success", "data": data}), 201

    # This handles the GET request to list all visitors
    if request.method == 'GET':
       
        visitors_str = r.lrange('visitors', 0, -1)
        
        visitors = [json.loads(v) for v in visitors_str]
        
        return jsonify(visitors)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5002)