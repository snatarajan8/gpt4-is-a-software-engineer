# github_files_service.py
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BASE_URL = "https://api.github.com/repos/snatarajan8/gpt4-is-a-software-engineer/git/trees/main?recursive=1"

@app.route('/files', methods=['GET'])
def get_files():
    r = requests.get(BASE_URL)
    files = [{"id": i, "path": file["path"]} for i, file in enumerate(r.json()["tree"])]
    return jsonify(files)

@app.route('/file/<int:file_id>', methods=['GET'])
def get_file(file_id):
    r = requests.get(BASE_URL)
    files = [{"id": i, "path": file["path"], "url": file["url"]} for i, file in enumerate(r.json()["tree"])]
    if file_id < len(files):
        return jsonify(files[file_id])
    return jsonify({"error": "File not found"}), 404

if __name__ == "__main__":
    app.run(port=5003)
