import random
from Data import art
from replit import clear

def compare(random_number, user_guess):
    if random_number == user_guess:
        print(f"You won, the number was {random_number}")
        return 1
    elif random_number > user_guess and random_number - user_guess > 5:
        print("Too Low")
        return 0
    elif user_guess - random_number > 5:
        print("Too High")
        return 0
    else:
        print("Close")
        return 0

def Get_Try_Count(difficulty_level):
    if difficulty_level == "easy":
        return 10
    elif difficulty_level == "hard":
        return 5
    else:
        print("Invalid Input")
        return 0

def Continue_Play():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    difficulty_level_input = input("Choose a difficulty, 'easy' or 'hard': ")
    
    try_count = Get_Try_Count(difficulty_level_input)
    random_number = random.randint(1, 100)

    while try_count > 0:
        print(f"You have {try_count} attempts remaining to guess the number.")
        guess = input("Make a Guess: ")
        result = compare(random_number, int(guess))
        if result == 1:
            break
        try_count = try_count - 1
        if try_count == 0:
            print(f"You lost. The number was {random_number}")

while(input("Do you want to play a game of Number Guessing? Type 'y' or 'n': ")):
    clear()
    Continue_Play()