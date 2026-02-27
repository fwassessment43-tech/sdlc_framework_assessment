'''
board.py
Provides the Board class responsible for rendering the game grid.
'''
import pygame
from constants import GameConfig
class Board:
    def __init__(self, config: GameConfig):
        self.config = config
    def draw(self, surface: pygame.Surface):
        '''Draws the grid lines over the background.'''
        surface.fill(self.config.BACKGROUND)
        for x in range(0, self.config.WIDTH, self.config.CELL_SIZE):
            pygame.draw.line(surface, self.config.GRID_LINES, (x, 0), (x, self.config.HEIGHT))
        for y in range(0, self.config.HEIGHT, self.config.CELL_SIZE):
            pygame.draw.line(surface, self.config.GRID_LINES, (0, y), (self.config.WIDTH, y))