import random

choices = ["rock", "paper", "scissors"]
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

userInput = str.lower(input("Pick a rock, paper scissors: "))

if userInput not in choices:
    print("Invalid")
else:
    cpuChoice = random.choice(choices)
    print(f"You: {userInput}")
    print(f"CPU: {cpuChoice}")

    if userInput == cpuChoice:
        print("Draw")
    elif beats[userInput] == cpuChoice:
        print("Win")
    else:
        print("Lose")

