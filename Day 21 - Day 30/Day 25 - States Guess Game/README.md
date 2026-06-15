# Day 25 - States Guess Game

This project is an interactive geography game that asks the user to name U.S. states and shows correct answers on a map. The game tracks progress and can save a list of states the player still needs to learn.

## What This Project Shows

* Displays a U.S. map using the Turtle graphics library.
* Accepts user input through a graphical text prompt.
* Reads state data from a CSV file and uses it to place labels on the map.
* Saves missing states to a new CSV file when the player exits early.

## How to Run

### Prerequisites

* Python 3.8 or newer

### Steps

1. Open the `Day 25 - States Guess Game` folder in your editor or file explorer.
2. Open a terminal or command prompt in the `Day 25 - States Guess Game` folder.
3. Ensure `main.py`, `50_states.csv`, and `blank_states_img.gif` are present in the folder.
4. Create a virtual environment in the project folder:

```bash
python -m venv venv
```

4. Activate the virtual environment:

```bash
.\venv\Scripts\Activate
```

5. Install the pandas library:

```bash
pip install pandas
```

6. Run the application.

### Run Command

```bash
python main.py
```

## Concepts Learnt

* **pandas** – Uses the pandas library to read CSV data into a DataFrame.
* **CSV file handling** – Loads state coordinates from `50_states.csv` and writes missing states to `states_to_learn.csv`.
* **DataFrame filtering** – Filters rows in a DataFrame to find the coordinates for a specific state.
