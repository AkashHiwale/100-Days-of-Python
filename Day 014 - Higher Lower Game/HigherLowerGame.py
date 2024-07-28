from Data import art, gamedata
import random
from replit import clear


def who_has_more_followers(first_person, second_person):
    if first_person > second_person:
        return "A"
    else:
        return "B"


def correct_user_response(user_input):
    if user_input == "A" or user_input == "a":
        return "A"
    elif user_input == "B" or user_input == "b":
        return "B"
    else:
        return "Invalid Response"


print(art.logo)
is_game_over = False
user_score = 0
person_a = random.choice(gamedata.data)
person_b = random.choice(gamedata.data)

while person_a == person_b:
    person_b = random.choice(gamedata.data)

while not is_game_over:
    print(f"Compare A: {person_a["name"]}, {person_a["description"]} from {person_a["country"]}.")
    print(art.vs)
    print(f"Against B: {person_b["name"]}, {person_b["description"]} from {person_b["country"]}.")

    output = who_has_more_followers(int(person_a["follower_count"]), int(person_b["follower_count"]))
    user_response = correct_user_response(input("Who has more followers? Type 'A' or 'B': "))

    is_game_over = False
    person_a = person_b
    person_b = random.choice(gamedata.data)
    while person_a == person_b:
        person_b = random.choice(gamedata.data)

    clear()
    print(art.logo)

    if output == user_response:
        user_score += 1
        print(f"You're right! Current Score: {user_score}")
    else:
        print(f"Sorry, that's wrong! Final Score: {user_score}")
        is_game_over = True
