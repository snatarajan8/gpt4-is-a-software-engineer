import json

HIGHSCORE_FILE = 'highscores.json'


def get_highscores():
    try:
        with open(HIGHSCORE_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_highscore(score):
    scores = get_highscores()
    scores.append(score)
    scores.sort(reverse=True)
    scores = scores[:10]  # Only top 10 scores

    with open(HIGHSCORE_FILE, 'w') as f:
        json.dump(scores, f)
