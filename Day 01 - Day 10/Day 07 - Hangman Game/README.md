# Hangman Game

A console-based word guessing game where the player tries to guess a hidden word one letter at a time before running out of lives.

## What This Project Shows

- Lets the player enter letters to guess a hidden word.
- Tracks correct and incorrect guesses to update game progress.
- Uses game state and lives to determine win or lose conditions.
- Imports data from local modules for word lists and ASCII art.

## How to Run

### Prerequisites

* Python 3.8 or newer
* Visual Studio Code (optional)

### Steps

1. Clone the repository.
2. Open the `Day 01 - Day 10/Day 07 - Hangman Game` folder.
3. Open a terminal in the project folder.
4. Run the application.

### Run Command

```bash
python HangmanGame.py
```

### Dependencies

> Note: This project uses only the standard library and does not require additional packages.

## Concepts Learnt

- **Importing from modules** – Uses `from Data import hangman_art` and `from Data import hangman_words` to load game assets.
- **Loops** – Uses a `while` loop to repeat guessing until the game ends.
- **List and string handling** – Builds and updates the word display using lists and joins list elements into strings.
- **Conditional logic** – Checks guess accuracy and updates lives and game status accordingly.
