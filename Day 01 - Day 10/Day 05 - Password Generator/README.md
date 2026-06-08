# Password Generator

A console utility that generates a random password from letters, numbers, and symbols based on the user's selected counts.

## What This Project Shows

- Accepts user input for the number of letters, symbols, and numbers.
- Builds a password by selecting random characters from character lists.
- Randomizes the final character order to improve password unpredictability.
- Outputs the generated password directly in the console.

## How to Run

### Prerequisites

* Python 3.8 or newer
* Visual Studio Code (optional)

### Steps

1. Clone the repository.
2. Open the `Day 01 - Day 10/Day 05 - Password Generator` folder.
3. Open a terminal in the project folder.
4. Run the application.

### Run Command

```bash
python PasswordGenerator.py
```

### Dependencies

> Note: This project uses only the standard library and does not require additional packages.

## Concepts Learnt

- **`for` loops** – Repeats actions for a specified number of characters requested by the user.
- **List building and `append()`** – Collects randomly selected letters, symbols, and numbers into a list.
- **`random.shuffle()`** – Randomizes the order of the generated password characters.
- **String assembly** – Combines individual list elements into a final password string.
