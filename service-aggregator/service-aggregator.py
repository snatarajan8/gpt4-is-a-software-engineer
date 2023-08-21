# service_aggregator.py
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/aggregate', methods=['GET'])
def aggregate():
    cpu_info = requests.get("http://localhost:5001/cpu_percent").json()
    devices = requests.get("http://localhost:5002/connected_devices").json()
    files = requests.get("http://localhost:5003/files").json()

    return jsonify({
        "cpu_info": cpu_info,
        "connected_devices": devices,
        "github_files": files
    })

if __name__ == "__main__":
    app.run(port=5000)
