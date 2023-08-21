# ui_service.py
from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/fetch/<service>/<endpoint>', methods=['GET'])
def fetch_data(service, endpoint):
    if service == "cpu":
        port = 5001
    elif service == "devices":
        port = 5002
    elif service == "github":
        port = 5003
    else:
        return jsonify({"error": "Invalid service"}), 404

    try:
        response = requests.get(f"http://localhost:{port}/{endpoint}")
        return response.json()
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5004, debug=True)
