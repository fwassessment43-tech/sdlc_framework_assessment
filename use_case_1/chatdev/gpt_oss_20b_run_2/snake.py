'''
snake.py
Defines the Snake class with movement, growth, and collision detection logic.
'''
import pygame
from constants import GameConfig
from typing import List, Tuple
# Direction vectors
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
OPPOSITE = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT
}
class Snake:
    def __init__(self, start_pos: Tuple[int, int], init_length: int = 3, direction: Tuple[int, int] = RIGHT):
        self.body: List[Tuple[int, int]] = [start_pos]
        self.direction = direction
        self.grow_pending = 0  # Number of segments to grow
        # Initialize body extending in opposite direction of movement
        for i in range(1, init_length):
            x, y = start_pos[0] - i * direction[0], start_pos[1] - i * direction[1]
            self.body.append((x, y))
        self.prev_head_pos = start_pos  # For animation
    def change_direction(self, new_dir: Tuple[int, int]):
        '''Change snake direction if not directly opposite.'''
        if new_dir and new_dir != OPPOSITE[self.direction]:
            self.direction = new_dir
    def move(self):
        '''Move snake by adding new head and removing tail unless growing.'''
        self.prev_head_pos = self.body[0]  # Store previous head for animation
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.body.insert(0, new_head)
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()
    def grow(self, segments: int = 1):
        '''Increase snake length by the given number of segments.'''
        self.grow_pending += segments
    def collides_with_self(self) -> bool:
        '''Check if head collides with any other body segment.'''
        return self.body[0] in self.body[1:]
    def collides_with_wall(self, config: GameConfig) -> bool:
        '''Check if head is outside the board boundaries.'''
        x, y = self.body[0]
        return not (0 <= x < config.GRID_SIZE and 0 <= y < config.GRID_SIZE)
    def draw(self, surface: pygame.Surface, config: GameConfig):
        '''Render the snake onto the given surface.'''
        for idx, (x, y) in enumerate(self.body):
            rect = pygame.Rect(x * config.CELL_SIZE, y * config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE)
            color = config.SNAKE_HEAD if idx == 0 else config.SNAKE_BODY
            pygame.draw.rect(surface, color, rect)