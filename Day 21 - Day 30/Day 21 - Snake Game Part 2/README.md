# Project Name

Snake Game — Part 2 is an enhanced, interactive version of the classic Snake game built with Python's turtle module. The player controls a snake that moves continuously, eats food to increase score, and must avoid colliding with walls or its own tail.

## What This Project Shows

- Accepts keyboard input to control the snake's direction.
- Continuous movement and frame updates using the `turtle` event loop and `screen.update()`.
- Spawning food items on the playfield and detecting collisions between the snake and food.
- Score tracking and on-screen scoreboard display with live updates.
- Collision detection for walls and the snake's own tail, resulting in game over.
- A modular design that separates responsibilities across `Snake`, `Food`, and `Scoreboard` classes.

## How to Run

### Prerequisites

 - Python 3.8 or newer
 - A system with a display (the `turtle` module requires a graphical environment)
 - Visual Studio Code (optional)

### Steps

1. Clone the repository.
2. Open the project folder.
3. Open a terminal in the folder `Day 21 - Day 30/Day 21 - Snake Game Part 2`.
4. Run the application.

### Run Command

```
python main.py
```

### Dependencies

> Note: This project uses only the standard library and does not require additional packages.

## Concepts Learnt


* **Inheritance (subclassing `Turtle`)** – Create custom on-screen objects by inheriting from the built-in `turtle.Turtle` class (for example, `class Food(Turtle)` and `class Scoreboard(Turtle)`) and initialize with `super().__init__()` to reuse drawing and movement behavior.
* **List slicing for segment iteration (`segments[1:]`)** – Use Python list slicing to obtain a subset of the snake's segments (e.g., `snake.segments[1:]`) so you can iterate over the tail separately from the head, which simplifies collision checks and segment management.
* **Shape sizing with `shapesize()`** – Adjust the displayed size of turtle shapes (used to create a smaller food item via `shapesize(stretch_len=0.5, stretch_wid=0.5)`).
* **Distance-based collision detection (`distance()`)** – Use the `Turtle.distance()` method to detect proximity between objects (for food consumption and tail collisions).
* **On-screen text updates using `clear()` and `write()`** – Maintain a dynamic scoreboard by clearing previous text and writing the updated score to the screen.
* **Dynamically extending game objects (snake growth)** – Add new segments to the snake at runtime to model growth when the snake eats food.
