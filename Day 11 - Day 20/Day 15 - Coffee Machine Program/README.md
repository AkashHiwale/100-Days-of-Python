# Coffee Machine Program

This project simulates a simple console coffee machine that lets users choose a drink, insert coins, and receive the beverage if enough ingredients and payment are available.

## What This Project Shows

- Accepts user input for beverage selection and operational commands.
- Uses nested dictionary data to define drink recipes, ingredient amounts, and prices.
- Checks available resources before making a drink and updates the inventory.
- Processes coin input, validates payment, and returns change when needed.

## How to Run

### Prerequisites

* Python 3.8 or newer
* Visual Studio Code (optional)

### Steps

1. Open the `Day 11 - Day 20/Day 15 - Coffee Machine Program` folder.
2. Open a terminal in the project folder.
3. Run the application.

### Run Command

```bash
python CoffeeMachineProgram.py
```

### Dependencies

> Note: This project uses only the standard library and does not require additional packages.

## Concepts Learnt

- **Nested dictionaries** – Organizes drink menu details with ingredient requirements and cost in a multi-level dictionary.
- **Resource management** – Tracks and reduces available ingredients as each drink is made.
- **Coin processing and transaction validation** – Converts coin counts into a payment total and checks whether it covers the drink cost.
- **Change calculation with rounding** – Computes the correct change amount and rounds it to two decimal places.
