'''
constants.py
This module defines game configuration constants used throughout the game.
'''
from dataclasses import dataclass
@dataclass(frozen=True)
class GameConfig:
    GRID_SIZE: int = 10           # 10x10 grid
    CELL_SIZE: int = 40           # each cell is 40x40 pixels
    WIDTH: int = GRID_SIZE * CELL_SIZE
    HEIGHT: int = GRID_SIZE * CELL_SIZE
    FPS: int = 10                 # game updates per second
    FLASH_DURATION: int = 300     # milliseconds for flash animations
    # Colors (R, G, B)
    BACKGROUND: tuple = (30, 30, 30)
    GRID_LINES: tuple = (50, 50, 50)
    SNAKE_HEAD: tuple = (0, 255, 0)
    SNAKE_BODY: tuple = (0, 200, 0)
    FOOD: tuple = (255, 0, 0)
    TEXT: tuple = (255, 255, 255)
    FLASH_HEAD: tuple = (255, 0, 0)