Play here - https://replit.com/@AkashHiwale/calculator-start#main.py
  
import art

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}


def calculator():
  print(art.logo)
  n1 = float(input("Enter the first number: "))

  for symbol in operations:
    print(symbol)

  should_continue = True

  while should_continue:

    operation_symbol = input("Pick the operation you want to perform: ")

    n2 = float(input("Enter the second number: "))

    result = operations[operation_symbol](n1, n2)

    print(f"{n1} {operation_symbol} {n2} = {result}")

    if input(f"Do you want to continue with {result} press 'y' or to start a new calculation press 'n': ") == "y":
      should_continue = True
      n1 = result
    else:
      should_continue = False
      calculator()

calculator()
