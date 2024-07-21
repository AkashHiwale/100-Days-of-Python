from replit import clear

from Data import art

print(art.logo)
record_dictionary = {}

value = True

def find_winner(record_dictionary):
  highest_bid = 0
  for key in record_dictionary:
    if record_dictionary[key] > highest_bid:
      highest_bid = record_dictionary[key]
      winner = key

  print(f"The winner is {winner} and the bid is {highest_bid}.")


while value:
  name = input("Enter your name: ")
  bid = int(input("Enter your bid: "))
  record_dictionary[name] = bid
  next = input("Are there any other bidders? Type 'yes' or 'no' ")

  if next == "yes":
    value = True
  else:
    value = False

  clear()

find_winner(record_dictionary)
