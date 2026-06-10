# Quiz Project

This project runs a console-based True/False quiz that asks a series of questions and tracks the user's score. It guides the user through each question, provides feedback, and displays a final score at the end.

## What This Project Shows

* Accepts user input from the console for quiz answers.
* Presents a sequence of True/False questions one at a time.
* Checks answers and gives immediate feedback after each response.
* Tracks the user's score as the quiz progresses.

## How to Run

### Prerequisites

* Python 3.8 or newer
* A terminal or command prompt

### Steps

1. Open the `Day 11 - Day 20/Day 17 - Quiz Project` folder.
2. Open a terminal in this folder.
3. Run the application.

### Run Command

```bash
python main.py
```

### Dependencies

> Note: This project uses only the standard library and does not require additional packages.

## Concepts Learnt

* **Modular imports** – Uses multiple files and imports to separate quiz data, question logic, and application flow.
* **Custom class model** – Defines a `Question` class to represent each quiz item with its text and correct answer.
* **Control flow with class methods** – Uses `QuizBrain` methods to manage question progression and score tracking.
* **Case-insensitive comparison** – Normalizes user input with `.lower()` to compare answers reliably.
