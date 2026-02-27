import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 10

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the clock
clock = pygame.time.Clock()

class SnakeGame:
    def __init__(self):
        self.snake_pos = [(200, 200), (220, 200), (240, 200)]
        self.direction = 'RIGHT'

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Fill the background with black
            win.fill(BLACK)

            # Draw the snake
            for pos in self.snake_pos:
                pygame.draw.rect(win, WHITE, (pos[0], pos[1], 20, 20))

            # Update the display
            pygame.display.update()

            # Cap the frame rate
            clock.tick(10)

if __name__ == '__main__':
    game = SnakeGame()
    game.run()