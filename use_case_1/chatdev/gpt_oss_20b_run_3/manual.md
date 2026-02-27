# Snake Game User Manual

## Table of Contents

- [Overview](#overview)
- [System Requirements](#system-requirements)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Running the Game](#running-the-game)
- [Gameplay & Controls](#gameplay--controls)
- [Features](#features)
- [Scoring](#scoring)
- [Game Over & Restart](#game-over--restart)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Overview

The **Snake Game** is a classic arcade-style game implemented in Python using the `pygame` library. The snake moves around a grid, eats food to grow longer, and must avoid colliding with walls or itself. This manual explains how to install, run, and play the game, and provides guidance on extending or customizing the code.

---

## System Requirements

| Item | Minimum | Recommended |
|------|---------|-------------|
| Operating System | Windows 7+, macOS 10.12+, Linux (Ubuntu 18.04+, Debian 10+) | Latest OS versions |
| CPU | 1 GHz or faster | 2 GHz or faster |
| RAM | 512 MB | 2 GB or more |
| Python | 3.7+ | 3.10+ |
| GPU | Any (CPU rendering is fine) | Any |

---

## Prerequisites

1. **Python** – The game is written in Python. Download it from the [official site](https://www.python.org/downloads/) if you don’t already have it installed.
2. **`pip`** – Python’s package installer, included with recent Python releases.
3. **`pygame`** – A 2‑D graphics library required to run the game.

> **Tip:** If you already use a virtual environment tool (e.g., `venv`, `conda`, `pipenv`), create one before installing the dependencies.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/snake-game.git
cd snake-game
```

> Replace the URL with the actual location of the source if you downloaded the files manually.

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv            # Windows
source venv/bin/activate      # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install pygame
```

> The game only depends on `pygame`. No other external libraries are required.

### 4. Verify the Installation

Run a quick test to ensure `pygame` works:

```bash
python - <<'PY'
import pygame
print(pygame.ver)
PY
```

You should see the pygame version printed.

---

## Project Structure

```
snake-game/
├── constants.py   # Grid, colors, FPS, etc.
├── snake.py       # Snake class logic
├── food.py        # Food generation logic
├── game.py        # Main game controller & loop
├── main.py        # Entry point
└── README.md
```

- **constants.py** – Holds configuration constants (grid size, cell size, colors, FPS, directions).
- **snake.py** – Encapsulates the snake’s state and movement logic.
- **food.py** – Manages food placement ensuring it never spawns on the snake.
- **game.py** – Orchestrates the game loop, rendering, input handling, and collision logic.
- **main.py** – Starts the game by creating a `Game` instance.

---

## Running the Game

Simply execute the `main.py` script:

```bash
python main.py
```

A window titled **"Snake Game"** will open, showing a 10 × 10 grid. The snake starts moving to the right immediately.

---

## Gameplay & Controls

| Key | Action |
|-----|--------|
| Arrow Up | Move the snake **up** |
| Arrow Down | Move the snake **down** |
| Arrow Left | Move the snake **left** |
| Arrow Right | Move the snake **right** |
| **R** (when game over) | Restart the game |

> The snake continues to move in its current direction until you change it with the arrow keys. You cannot reverse direction instantly (e.g., from left to right).

**In‑Game Instructions**

When the game is running, a text overlay at the bottom says:

```
Use arrow keys to move. Eat food to grow.
```

This reminds you of the core objective.

---

## Features

- **Grid-Based Display** – The game board is a 10×10 grid, each cell 40×40 pixels.
- **Automatic Movement** – The snake moves automatically at a fixed FPS (10 fps by default).
- **Food Placement** – Food spawns at random positions, never overlapping the snake.
- **Collision Detection** – The game ends if the snake hits the walls or its own body.
- **Growth Mechanic** – Eating food increases the snake’s length by one segment.
- **Scoring System** – Each food item eaten increases the score by one.
- **Game Over Overlay** – Semi‑transparent overlay with “GAME OVER” and restart prompt.
- **Restart Capability** – Press **R** to start a fresh game without restarting the program.

---

## Scoring

The current score is displayed at the top‑left corner:

```
Score: <number>
```

Every time the snake consumes food, the score increments by 1. The maximum possible score depends on how many food items the snake can eat before filling the board.

---

## Game Over & Restart

- **Game Over** – Triggered when:
  - The snake’s head moves beyond the grid boundaries.
  - The snake’s head collides with its own body.
  - The grid is completely filled with the snake (no space for new food).
- **Overlay** – A semi‑transparent black overlay appears with two messages:
  - “GAME OVER”
  - “Press R to Restart”
- **Restart** – Press **R** at any time after the game over to reset the snake, food, score, and start a new session.

---

## Customization

You can easily tweak game parameters by editing **constants.py**:

- `GRID_SIZE` – Change the number of cells (e.g., `GRID_SIZE = 20` for a 20×20 grid).
- `CELL_SIZE` – Adjust pixel size of each cell (e.g., `CELL_SIZE = 30`).
- `FPS` – Increase to make the snake faster (`FPS = 20`) or decrease for slower gameplay.
- `COLORS` – Modify RGB values to change the appearance.
- `DIRECTIONS` – Add new movement directions or rename keys if needed.

**Example: Faster Snake**

```python
# constants.py
FPS = 20   # Double the speed
```

After changing, restart the game to see the new speed.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Game window does not appear | `pygame` not installed or mis‑configured | Run `pip install pygame` |
| Game freezes or crashes | Out‑of‑date Python/pygame | Update to the latest Python 3.x and `pip install --upgrade pygame` |
| Snake moves too fast/slow | FPS mismatch | Adjust `FPS` in `constants.py` |
| Food spawns on snake | Logic error in `Food.generate()` | Verify `snake_body` is correctly passed; the provided code handles this case. |
| Cannot restart | Key binding missing | Ensure `event.key == pygame.K_r` in `game.py`'s event handling |

If you encounter an error you cannot resolve, open an issue on the project's repository or ask for help in the community.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details. Feel free to modify, share, or build upon it.

---