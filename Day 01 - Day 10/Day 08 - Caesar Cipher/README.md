# Caesar Cipher

A console application that encrypts and decrypts text by shifting letters through the alphabet using the Caesar cipher method.

## What This Project Shows

- Accepts user input for encoding or decoding a message.
- Applies a shift to alphabet letters while preserving non-letter characters.
- Uses a function to encapsulate the cipher logic.
- Repeats the process until the user chooses to stop.

## How to Run

### Prerequisites

* Python 3.8 or newer
* Visual Studio Code (optional)

### Steps

1. Clone the repository.
2. Open the `Day 01 - Day 10/Day 08 - Caesar Cipher` folder.
3. Open a terminal in the project folder.
4. Run the application.

### Run Command

```bash
python CaesarCipher.py
```

### Dependencies

> Note: This project uses only the standard library and does not require additional packages.

## Concepts Learnt

- **Functions** – Defines `caesar()` to encapsulate and reuse the cipher logic.
- **Alphabet mapping** – Uses a duplicated alphabet list to shift letter positions and wrap around the alphabet.
- **Modular arithmetic** – Applies `shift % 25` to constrain the shift value within the alphabet range.
