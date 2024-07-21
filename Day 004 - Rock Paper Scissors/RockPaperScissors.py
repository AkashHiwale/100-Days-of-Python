import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if user_input != "0" and user_input != "1" and user_input != "2":
  print("Invalid input. Game over.")
else:
  if user_input == "0":
    print(rock)
  elif user_input == "1":
    print(paper)
  elif user_input == "2":
    print(scissors)
  
  print("Computer chose: \n")
  computer_choice = random.choice(options)
  print(computer_choice);
  
  if computer_choice == rock and user_input == "2":
    print("You lose. Better luck next time.")
  elif computer_choice == rock and user_input == "1":
    print("You win.")
  elif computer_choice == paper and user_input == "2":
    print("You lose. Better luck next time.")
  elif computer_choice == paper and user_input == "0":
    print("You win.")
  elif computer_choice == scissors and user_input == "1":
    print("You lose. Better luck next time.")
  elif computer_choice == scissors and user_input == "0":
    print("You win.")
  else:
    print("Draw.")
