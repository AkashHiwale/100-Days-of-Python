import random
from replit import clear
from Data import art

# Method to randomly get one card
def deal_card():
    card_options = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    choosen_card = random.choice(card_options)
    return choosen_card

# Method to calculate total score from a list of cards
def total_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Method to compare final score of user and opponent and return the final result
def compare(user_score, computer_score):
    if(user_score == computer_score):
        return "It's a draw"
    elif(computer_score == 0):
        return "You lost, Opponent hit a BlackJack."
    elif(user_score == 0):
        return "You won, You hit a BlackJack"
    elif(user_score > 21):
        return "You lost, you went over."
    elif(computer_score > 21):
        return "You win, Opponent went over."
    elif(user_score > computer_score):
        return "You win"
    else:
        return "You lose"

def play_game():

    print(art.logo)

    # Intializing empty lists for user and computer
    computer_cards = []
    user_cards = []
    is_game_over = False

    # Randomly selecting two cards for user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = total_score(user_cards)
        computer_score = total_score(computer_cards)
        print(f"Your current cards: {user_cards}, total: {user_score}")
        print(f"Opponent first card is: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or 'n' to pass: ") 
            if(user_should_deal == 'y'):
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = total_score(computer_cards)

    print(f"Your final cards: {user_cards}, total: {user_score}")
    print(f"Opponent final cards: {computer_cards}, total: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()