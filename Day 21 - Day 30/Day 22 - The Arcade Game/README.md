# Project Name

A two-player arcade-style paddle-and-ball game built with Python's `turtle` module. Players control paddles to keep the ball in play and score points when the opponent misses.

## What This Project Shows

- Two-player keyboard controls (right player: Arrow Up/Down; left player: `w`/`s`).
- A modular, object-oriented design using `Ball`, `Paddle`, and `Scoreboard` classes that subclass `turtle.Turtle`.
- Simple ball physics: continuous movement, bouncing off walls and paddles, and resetting after a score.
- Collision detection using position checks and proximity (`distance()` and coordinate thresholds).
- A basic game loop with manual frame updates using `screen.update()` and `time.sleep()`.
- On-screen score display using `clear()` and `write()` to update scores.

## How to Run

### Prerequisites

- Python 3.8 or newer
- A system with a graphical display (the `turtle` module requires a GUI environment)
- Visual Studio Code (optional)

### Steps

1. Clone the repository.
2. Open the project folder.
3. Open a terminal in `Day 21 - Day 30/Day 22 - The Arcade Game`.
4. Run the application.

### Run Command

```
python main.py
```

### Dependencies

> Note: This project uses only the standard library and does not require additional packages.

## Concepts Learnt

No new technical concepts were introduced in this lesson.
