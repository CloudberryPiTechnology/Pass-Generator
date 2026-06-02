import random

def generate(length=8):
    letters = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(letters)
    password = []
    for _ in range(length):
        password.append(random.choice(letters))
    return "".join(password)

# Example:
print(generate(12))
