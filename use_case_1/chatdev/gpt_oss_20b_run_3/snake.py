'''
snake.py
'''
from constants import GRID_SIZE, DIRECTIONS
class Snake:
    """
    Represents the snake in the game.
    Attributes
    ----------
    body : list of tuple
        List of coordinates (x, y) for each segment, head is first element.
    direction : tuple
        Current movement direction (dx, dy).
    grow_flag : bool
        When True the snake will grow on the next move.
    """
    def __init__(self, initial_pos, initial_length=3):
        self.body = [initial_pos]
        self.direction = DIRECTIONS['RIGHT']
        self.grow_flag = False
        # Add initial segments to the left of the head
        for i in range(1, initial_length):
            self.body.append((initial_pos[0] - i, initial_pos[1]))
    def set_direction(self, new_dir):
        """
        Change direction only if it is not directly opposite to current.
        """
        opposite = (-self.direction[0], -self.direction[1])
        if new_dir != opposite:
            self.direction = new_dir
    def move(self):
        """
        Move snake forward in current direction, handle growth.
        """
        new_head = (self.head()[0] + self.direction[0],
                    self.head()[1] + self.direction[1])
        self.body.insert(0, new_head)
        if self.grow_flag:
            self.grow_flag = False
        else:
            self.body.pop()
    def grow(self):
        """
        Flag the snake to grow on the next move.
        """
        self.grow_flag = True
    def head(self):
        """
        Return the coordinate of the snake's head.
        """
        return self.body[0]
    def collides_with_self(self):
        """
        Return True if the head collides with any other segment.
        """
        return self.head() in self.body[1:]
    def collides_with_boundary(self):
        """
        Return True if the head is outside the grid boundaries.
        """
        x, y = self.head()
        return x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE