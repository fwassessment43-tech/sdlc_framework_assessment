'''
food.py
Handles food generation, placement, and rendering with flash animation.
'''
import random
import pygame
from constants import GameConfig
from typing import Tuple
from snake import Snake
class Food:
    def __init__(self, config: GameConfig, snake: Snake):
        self.config = config
        self.snake = snake
        self.position = self._random_position()
        self.flash_end_time = 0  # When the flash effect ends
    def _random_position(self) -> Tuple[int, int]:
        '''Return a random grid position not occupied by the snake.'''
        available = [(x, y) for x in range(self.config.GRID_SIZE)
                              for y in range(self.config.GRID_SIZE)
                              if (x, y) not in self.snake.body]
        if not available:
            return (0, 0)  # Should never happen in normal play
        return random.choice(available)
    def reposition(self):
        '''Generate a new position for the food.'''
        self.position = self._random_position()
    def start_flash(self, current_time: int):
        '''Begin a flash effect for a short duration.'''
        self.flash_end_time = current_time + self.config.FLASH_DURATION
    def draw(self, surface: pygame.Surface, current_time: int):
        '''Render the food onto the given surface, with flashing if active.'''
        x, y = self.position
        rect = pygame.Rect(x * self.config.CELL_SIZE, y * self.config.CELL_SIZE,
                           self.config.CELL_SIZE, self.config.CELL_SIZE)
        # If flashing, make food brighter
        if current_time < self.flash_end_time:
            color = tuple(min(255, int(c * 1.5)) for c in self.config.FOOD)
            size = int(self.config.CELL_SIZE * 1.2)
            # Clamp offset to non‑negative to avoid rectangle starting outside the cell
            offset = max(0, (self.config.CELL_SIZE - size) // 2)
            rect = pygame.Rect(x * self.config.CELL_SIZE + offset,
                               y * self.config.CELL_SIZE + offset,
                               size, size)
        else:
            color = self.config.FOOD
        pygame.draw.rect(surface, color, rect)