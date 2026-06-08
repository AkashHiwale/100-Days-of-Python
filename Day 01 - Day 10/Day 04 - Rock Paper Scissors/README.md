# Rock Paper Scissors

A console game where the user selects rock, paper, or scissors and plays a single round against a computer-generated choice.

## What This Project Shows

- Accepts a numeric choice from the user for rock, paper, or scissors.
- Generates a random computer choice using the standard library.
- Compares the user’s selection with the opponent’s selection to determine the outcome.
- Handles invalid input and ends the game cleanly if the choice is not valid.

## How to Run

### Prerequisites

* Python 3.8 or newer
* Visual Studio Code (optional)

### Steps

1. Clone the repository.
2. Open the `Day 01 - Day 10/Day 04 - Rock Paper Scissors` folder.
3. Open a terminal in the project folder.
4. Run the application.

### Run Command

```bash
python RockPaperScissors.py
```

### Dependencies

> Note: This project uses only the standard library and does not require additional packages.

## Concepts Learnt

- **Lists** – Stores the available game options so the program can choose and display them.
- **Random selection** – Uses `random.choice()` to select the computer’s move from a list.
- **Input validation** – Checks that user input matches expected values before continuing.
