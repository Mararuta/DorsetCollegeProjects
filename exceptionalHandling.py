import random

RESPONSES = [
    "It is certain.",
    "without a doubt.",
    "most likely.",
    "Ask again later.",
    "Cannot predict now.",
    "Don't count on it.",
    "my reply is no.",
    "very doubtful."
]

def get_eight_ball_response():
    return random.choice(RESPONSES) 