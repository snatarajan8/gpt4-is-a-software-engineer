import csv
from instabot import Bot

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
        # Placeholder logic for validation
        if self._validate_user(user):
            users = self._load_users()
            users.append([user])
            self._save_users(users)

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

    def message_all(self, message):
        users = self._load_users()
        self.send_message([u[0] for u in users], message)

    def message_subset(self, subset_users, message):
        self.send_message(subset_users, message)


if __name__ == "__main__":
    USERNAME = "YOUR_INSTAGRAM_USERNAME"
    PASSWORD = "YOUR_INSTAGRAM_PASSWORD"

    insta_bot = InstagramBot(USERNAME, PASSWORD)

    # Test commands
    # insta_bot.add_user("example_user")
    # insta_bot.remove_user("example_user")
    # insta_bot.message_all("Hello, all!")
    # insta_bot.message_subset(["example_user1", "example_user2"], "Hello, subset!")
