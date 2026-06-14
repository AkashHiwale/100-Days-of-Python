# Project Name

Turtle Crossing Game — An interactive Turtle graphics game where the player guides a turtle across a busy road, avoiding oncoming cars to progress through levels.

## What This Project Shows
- Accepts keyboard input to control a player character (`Up` key to move the turtle).
- Dynamically spawns multiple moving obstacles (cars) that travel across the screen.
- Detects collisions between the player and obstacles to end the game.
- Tracks and displays the current level, increasing difficulty after each successful crossing.
- Uses a simple game loop with animation control via screen updates and timed sleeps.

## How to Run

### Prerequisites

- Python 3.8 or newer
- The standard library `turtle` module (included with CPython installations)

### Steps

1. Open a terminal.
2. Change directory into the project folder for Day 23:

```
cd "Day 21 - Day 30/Day 23 - Turtle Crossing Game"
```
3. Run the application.

### Run Command

```
python main.py
```

### Dependencies

> Note: This project uses only the standard library and does not require additional packages.

## Concepts Learnt

- **Dynamic obstacle spawning (probabilistic spawn)** – Cars are created at runtime using a random probability check to control spawn rate, producing unpredictable obstacle patterns.
- **Runtime object management (lists of objects)** – Newly created car objects are stored in a list and iterated each frame to update movement and check collisions.
- **Difficulty scaling** – Game difficulty increases over time by raising the movement speed of obstacles after each successful crossing.
- **Turtle shape scaling (`shapesize`)** – The `Turtle.shapesize()` method is used to change the turtle shape proportions (e.g., making rectangular car sprites).