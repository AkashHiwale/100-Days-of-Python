# NATO Alphabet Project

This project converts a user-entered word into its NATO phonetic alphabet spelling using a CSV data source.

## What This Project Shows

* Reads a CSV file and builds a lookup dictionary from its contents.
* Accepts user input from the console.
* Converts each letter of the input word into a phonetic code word.
* Displays the resulting phonetic alphabet sequence.

## How to Run

### Prerequisites

* Python 3.8 or newer
* `pandas` library
* Visual Studio Code (optional)

### Steps

1. Clone the repository.
2. Open the project folder: `Day 21 - Day 30\Day 26 - NATO Alphabet Project`.
3. Open a terminal in that folder.
4. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

5. Activate the virtual environment:

    ```bash
    .\venv\Scripts\activate
    ```

6. Install the required package:

   ```bash
   pip install pandas
   ```

7. Run the application.

### Run Command

```bash
python main.py
```


## Concepts Learnt

* **Dictionary comprehensions** – Used to build the `phonetic_dict` mapping from CSV rows.
* **List comprehensions** – Used to create the phonetic alphabet output list from the input word.
