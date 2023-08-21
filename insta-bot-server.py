import csv
from instabot import Bot
from flask import Flask, request, jsonify

app = Flask(__name__)

class InstagramBot:

    def __init__(self, username, password):
        self.bot = Bot()
        self.bot.login(username=username, password=password)

    def _load_users(self):
        with open('users.csv', 'r') as f:
            reader = csv.reader(f)
            return list(reader)

    def _save_users(self, users):
        with open('users.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(users)

    def add_user(self, user):
        if self._validate_user(user):
            users = self._load_users()
            users.append([user])
            self._save_users(users)
            return True
        return False

    def _validate_user(self, user):
        # TODO: Implement your validation logic here
        return True

    def remove_user(self, user):
        users = self._load_users()
        users = [u for u in users if u[0] != user]
        self._save_users(users)

    def send_message(self, users, message):
        for user in users:
            self.bot.send_message(message, [user])


# Flask routes
@app.route('/add_user', methods=['POST'])
def add_user():
    user = request.json.get('user')
    if insta_bot.add_user(user):
        return jsonify({"success": True, "message": "User added successfully!"}), 200
    return jsonify({"success": False, "message": "Failed to add user."}), 400

@app.route('/remove_user', methods=['POST'])
def remove_user():
    user = request.json.get('user')
    insta_bot.remove_user(user)
    return jsonify({"success": True, "message": "User removed successfully!"}), 200

@app.route('/send_message', methods=['POST'])
def send_message():
    users = request.json.get('users')
    message = request.json.get('message')
    insta_bot.send_message(users, message)
    return jsonify({"success": True, "message": "Message sent successfully!"}), 200


if __name__ == "__main__":
    USERNAME = "YOUR_INSTAGRAM_USERNAME"
    PASSWORD = "YOUR_INSTAGRAM_PASSWORD"

    insta_bot = InstagramBot(USERNAME, PASSWORD)

    app.run(debug=True)
