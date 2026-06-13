# Snake Game Part 1

A simple graphical Snake game using Python Turtle where the player controls the snake with arrow keys and watches it move across the screen.

## What This Project Shows

* Creates an interactive game window using Python Turtle.
* Uses keyboard input to control game movement.
* Implements a moving snake made of connected segments.
* Updates the display inside a continuous game loop.

## How to Run

### Prerequisites

* Python 3.8 or newer
* No additional packages are required

### Steps

1. Clone the repository.
2. Open the `Day 11 - Day 20/Day 20 - Snake Game Part 1` folder.
3. Open a terminal in that folder.
4. Run the application.

### Run Command

```bash
python main.py
```

### Dependencies

> Note: This project uses only the standard library and does not require additional packages.

## Concepts Learnt

* **Keyboard event handling** – Uses `screen.listen()` and `screen.onkey()` to respond to arrow key presses.
* **Game loop animation** – Uses a while loop with `screen.update()` and `time.sleep()` to animate the snake.
* **Segment-based movement** – Moves each snake segment to the position of the segment ahead of it for smooth motion.
