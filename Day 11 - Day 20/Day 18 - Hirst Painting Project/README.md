# Hirst Painting Project

This project draws a grid of colored dots using the Python Turtle graphics library. It creates a visual pattern inspired by Hirst-style dot paintings and displays it in a drawing window.

## What This Project Shows

* Uses Turtle graphics to draw shapes on the screen.
* Generates a grid of dots with randomized colors.
* Demonstrates how to control drawing position and movement.
* Uses a list of RGB color values and the random module to select colors dynamically.

## How to Run

### Prerequisites

* Python 3.8 or newer
* A terminal or command prompt

### Steps

1. Open the project folder in your editor or file explorer.
2. Open a terminal in the `Day 18 - Hirst Painting Project` folder.
3. Run the application using Python.
4. Click the Turtle graphics window to close it.

### Run Command

```bash
python main.py
```

### Dependencies

> Note: This project uses only the standard library and does not require additional packages.

## Concepts Learnt

* **Tuples** – Immutable sequences used to store fixed collections of values, such as RGB color coordinates (e.g., `(228, 227, 225)`).
* **Turtle graphics** – Uses the `turtle` module to create drawings in a graphical window.
* **RGB color mode** – Configures the drawing screen to use RGB color values with `screen.colormode(255)`.
* **Drawing control** – Moves the turtle, places dots, and adjusts coordinates to form a grid pattern.
* **Random selection** – Uses `random.choice()` to pick colors from a predefined list.
