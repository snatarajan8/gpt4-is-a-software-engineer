import os
import json
from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)

GPT3_ENDPOINT = "https://api.openai.com/v1/engines/davinci/completions"
API_KEY = "YOUR_OPENAI_API_KEY"  # Replace with your GPT-3 API key
LOG_FILE = "gpt3_prompts_responses.json"
LOGGING_FILE = "gpt3_api_server.log"

# Setting up logging
logging.basicConfig(filename=LOGGING_FILE, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

@app.route('/ask-gpt3', methods=['POST'])
def ask_gpt3():
    try:
        prompt = request.json.get("prompt")
        if not prompt:
            msg = "Prompt is required!"
            logger.error(msg)
            return jsonify({"error": msg}), 400

        data = {
            "prompt": prompt,
            "max_tokens": 150  # You can adjust this or add more parameters
        }

        response = requests.post(GPT3_ENDPOINT, headers=headers, json=data)

        if response.status_code != 200:
            msg = f"Failed to get response from GPT-3. Status code: {response.status_code}, Response: {response.text}"
            logger.error(msg)
            return jsonify({"error": "Failed to get response from GPT-3"}), 500

        gpt3_response = response.json().get("choices")[0].get("text").strip()

        # Log the prompt and response to a JSON file
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r') as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append({
            "prompt": prompt,
            "response": gpt3_response
        })

        with open(LOG_FILE, 'w') as f:
            json.dump(logs, f, indent=4)

        logger.info(f"Received response for prompt '{prompt}' successfully.")
        return jsonify({"response": gpt3_response})

    except Exception as e:
        logger.exception("An error occurred while processing the request.")
        return jsonify({"error": "An internal server error occurred."}), 500


if __name__ == "__main__":
    app.run(port=5000, debug=True)
