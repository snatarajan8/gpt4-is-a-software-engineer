# cpu_info_service.py
from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/cpu_percent', methods=['GET'])
def cpu_percent():
    return jsonify({"cpu_percent": psutil.cpu_percent()})

@app.route('/cpu_stats', methods=['GET'])
def cpu_stats():
    return jsonify(psutil.cpu_stats()._asdict())

@app.route('/cpu_count', methods=['GET'])
def cpu_count():
    return jsonify({"logical": psutil.cpu_count(logical=True), "physical": psutil.cpu_count(logical=False)})

@app.route('/cpu_freq', methods=['GET'])
def cpu_freq():
    return jsonify(psutil.cpu_freq()._asdict())

@app.route('/cpu_times_percent', methods=['GET'])
def cpu_times_percent():
    return jsonify(psutil.cpu_times_percent()._asdict())

if __name__ == "__main__":
    app.run(port=5001)
