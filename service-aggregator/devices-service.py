# devices_service.py
from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/connected_devices', methods=['GET'])
def connected_devices():
    return jsonify(psutil.disk_partitions())

@app.route('/device_usage/<path:device_path>', methods=['GET'])
def device_usage(device_path):
    try:
        usage = psutil.disk_usage(device_path)._asdict()
        return jsonify(usage)
    except FileNotFoundError:
        return jsonify({"error": "Device path not found"}), 404

@app.route('/device_io_counters', methods=['GET'])
def device_io_counters():
    return jsonify(psutil.disk_io_counters(perdisk=True, nowrap=True))

@app.route('/device_io_stats', methods=['GET'])
def device_io_stats():
    return jsonify(psutil.disk_io_counters()._asdict())

if __name__ == "__main__":
    app.run(port=5002)
