'''
food.py
'''
import random
from constants import GRID_SIZE
class Food:
    """
    Represents food in the snake game.
    Attributes
    ----------
    position : tuple
        Current coordinate of the food.
    """
    def __init__(self, snake_body):
        self.position = None
        self.generate(snake_body)
    def generate(self, snake_body):
        """
        Pick a random grid cell not occupied by the snake.
        If the snake fills the entire board, end the game gracefully.
        """
        empty_cells = [
            (x, y) for x in range(GRID_SIZE)
            for y in range(GRID_SIZE) if (x, y) not in snake_body
        ]
        if not empty_cells:
            # No space left for new food; set position to None
            self.position = None
            return
        self.position = random.choice(empty_cells)