# Snake Game User Manual

> **Version** 1.0.0 – February 2026  
> **Author**: Chief Product Officer, Snake Games Inc.  
> **License**: MIT

---

## Table of Contents

1. [Overview](#overview)  
2. [System Requirements](#system-requirements)  
3. [Installation](#installation)  
4. [Running the Game](#running-the-game)  
5. [Controls & Gameplay](#controls--gameplay)  
6. [Scoring & Progress](#scoring--progress)  
7. [Game Over & Restart](#game-over--restart)  
8. [Code Architecture](#code-architecture)  
9. [Extending the Game](#extending-the-game)  
10. [Troubleshooting](#troubleshooting)  
11. [FAQ](#faq)  

---

## 1. Overview

The **Python Snake Game** is a lightweight, grid‑based arcade classic built with the Pygame library. It demonstrates key concepts such as:

- Real‑time input handling  
- Continuous movement with smooth animation  
- Collision detection (walls, self, food)  
- Dynamic food generation  
- Score tracking & persistent game state  

The game is fully written in pure Python and is distributed as a single, self‑contained repository.

---

## 2. System Requirements

| Item                     | Minimum Requirement | Notes                           |
|--------------------------|---------------------|---------------------------------|
| **Operating System**     | Windows 7+, macOS 10.12+, Linux (Ubuntu 18.04+, Fedora 30+) | Cross‑platform with Pygame. |
| **Python**               | 3.8 or newer        | Tested on 3.10, 3.11, 3.12.     |
| **Pygame**               | 2.5.0 or newer      | Handles rendering & input.      |
| **Memory**               | 512 MB RAM          | Game is lightweight.            |
| **CPU**                  | 1 GHz+              | Real‑time loop runs at 60 FPS.  |

---

## 3. Installation

### 3.1 Clone the Repository

```bash
git clone https://github.com/your-org/snake-game.git
cd snake-game
```

> If you prefer, you can download the zip and extract it.

### 3.2 Create a Virtual Environment (recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3.3 Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> **requirements.txt** contains:

```text
pygame>=2.5.0
```

If you prefer installing manually:

```bash
pip install pygame
```

### 3.4 Verify Installation

```bash
python -c "import pygame, sys; print('Pygame version:', pygame.__version__)"
```

You should see a version string like `2.5.0`.

---

## 4. Running the Game

Simply run the entry point:

```bash
python main.py
```

A window titled **“Snake Game”** will open, sized 400 × 400 pixels by default (10 × 10 grid with 40 px cells).

> **Tip**: The game uses a fixed frame‑rate of 60 FPS for smooth input. FPS is independent of the logical update rate (10 updates per second).

---

## 5. Controls & Gameplay

| Key | Action |
|-----|--------|
| **Arrow Keys** | Change the snake’s direction (cannot reverse instantly). |
| **R** | Restart the game *only* after a game‑over. |
| **Esc / Window Close** | Exit the application. |

### 5.1 Movement

- The snake starts moving right automatically.
- Arrow keys adjust direction; the snake continues to move continuously until the next key press.
- The head is rendered in green; body segments are darker green.
- The head also flashes red when a collision occurs.

### 5.2 Food

- Food appears as a red square.  
- Upon consumption, the snake grows by one segment, and the score increments.
- Food flashes brighter briefly to indicate consumption.

### 5.3 Boundaries & Self‑Collision

- Colliding with the grid boundary or the snake’s own body ends the game.

---

## 6. Scoring & Progress

- **Score**: Displayed top‑left, updates each time food is eaten.
- The score is not persisted beyond the current run.
- No high‑score table; you can extend this by storing scores in a file or database.

---

## 7. Game Over & Restart

When a collision occurs:

1. A **“GAME OVER”** message appears in the center.
2. Press **R** to reset the snake, food, and score.
3. The game returns to the initial state and starts moving right again.

---

## 8. Code Architecture

```
snake-game/
├── constants.py     # Global game constants (grid size, colors, FPS, etc.)
├── board.py         # Renders the background grid
├── snake.py         # Snake logic: movement, growth, collision
├── food.py          # Food placement and flash animation
├── game.py          # Main game loop, event handling, rendering
└── main.py          # Application entry point
```

### Key Classes

| Class | Responsibility |
|-------|----------------|
| `GameConfig` | Immutable configuration holder |
| `Board` | Draws grid lines on the surface |
| `Snake` | Maintains body segments, direction, growth, collisions |
| `Food` | Generates random positions, handles flashing |
| `Game` | Orchestrates updates, rendering, input, and state transitions |

---

## 9. Extending the Game

You can enhance the game by modifying or adding modules:

| Feature | How to Implement |
|---------|------------------|
| **Custom Grid Size** | Change `GameConfig.GRID_SIZE` and adjust `CELL_SIZE` accordingly. |
| **Different FPS** | Edit `GameConfig.FPS` or adjust `move_interval` in `Game`. |
| **Speed Increase** | After every N food items, reduce `move_interval`. |
| **Score Persistence** | Store `self.score` in a file (e.g., JSON) in `Game.reset_game()` and `Game.update()`. |
| **Multiple Food Types** | Add a `type` attribute to `Food` and adjust score/behaviour. |
| **Sound Effects** | Load `.wav` files in `Game.__init__` and play on events. |
| **Higher‑Resolution Graphics** | Replace rectangles with sprites. |
| **AI Agent** | Replace manual key handling with an AI controller. |

> **Tip**: Always keep `constants.py` as the single source of truth for configuration to avoid scattering magic numbers.

---

## 10. Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Window opens but nothing appears | Pygame not initialized correctly | Ensure `pygame.init()` runs before creating the window |
| Game freezes on arrow key | Direction change logic prevents immediate reversal | Verify `Snake.change_direction()` logic |
| Food appears on snake body | `Food._random_position()` incorrectly excludes snake | Confirm `self.snake.body` is updated before repositioning |
| Application crashes on exit | Pygame surfaces not released | Use `pygame.quit()` before `sys.exit()` (already handled in `game.py`) |
| Performance issues on slow PC | Excessive drawing in `render()` | Reduce `move_interval` or limit FPS in `clock.tick()` |

---

## 11. FAQ

**Q1: Can I play on a larger screen?**  
A1: Yes, modify `GameConfig.GRID_SIZE` and `GameConfig.CELL_SIZE`. The window size will adjust automatically.

**Q2: Why is the snake speed fixed?**  
A2: The snake updates at `GameConfig.FPS` (10 updates per second). If you want a faster snake, increase `GameConfig.FPS` or decrease `move_interval`.

**Q3: How do I add sound?**  
A3: Load sound files using `pygame.mixer.Sound()` and play them in response to events (e.g., eating food or colliding).

**Q4: Is there an AI to play automatically?**  
A4: Not yet, but you can replace the key‑handler with an AI algorithm that sets `Snake.direction` each frame.

**Q5: How do I report bugs?**  
A5: Open an issue on the GitHub repository and provide a minimal reproducible example and environment details.

---

**Enjoy your game!** If you have questions or suggestions, feel free to open a discussion in the project’s issue tracker.