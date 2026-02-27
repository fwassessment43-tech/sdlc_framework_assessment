import pygame
import sys
import random

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
        self.score = 0
        self.food_pos = self.generate_food()

    def generate_food(self):
        while True:
            food_pos = (random.randint(0, WIDTH - 20) // 20 * 20,
                          random.randint(0, HEIGHT - 20) // 20 * 20)
            if food_pos not in self.snake_pos:
                return food_pos

    def update_score(self):
        self.score += 1

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != 'DOWN':
                        self.direction = 'UP'
                    elif event.key == pygame.K_DOWN and self.direction != 'UP':
                        self.direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                        self.direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                        self.direction = 'RIGHT'

            # Move the snake
            head_pos = self.snake_pos[-1]
            if self.direction == 'UP':
                new_head_pos = (head_pos[0], head_pos[1] - 20)
            elif self.direction == 'DOWN':
                new_head_pos = (head_pos[0], head_pos[1] + 20)
            elif self.direction == 'LEFT':
                new_head_pos = (head_pos[0] - 20, head_pos[1])
            elif self.direction == 'RIGHT':
                new_head_pos = (head_pos[0] + 20, head_pos[1])

            self.snake_pos.append(new_head_pos)

            # Check for collision with food
            if self.snake_pos[-1] == self.food_pos:
                self.update_score()
                self.food_pos = self.generate_food()
            else:
                self.snake_pos.pop(0)

            # Check for collision with boundaries or itself
            if (self.snake_pos[-1][0] < 0 or self.snake_pos[-1][0] >= WIDTH or
                    self.snake_pos[-1][1] < 0 or self.snake_pos[-1][1] >= HEIGHT or
                    self.snake_pos[-1] in self.snake_pos[:-1]):
                print("Game Over! Final Score:", self.score)
                pygame.quit()
                sys.exit()

            # Fill the background with black
            win.fill(BLACK)

            # Draw the snake
            for pos in self.snake_pos:
                pygame.draw.rect(win, WHITE, (pos[0], pos[1], 20, 20))

            # Draw the food
            pygame.draw.rect(win, (255, 0, 0), (self.food_pos[0], self.food_pos[1], 20, 20))

            # Display the score
            text = font.render("Score: " + str(self.score), True, WHITE)
            win.blit(text, (10, 10))

            # Update the display
            pygame.display.update()

            # Cap the frame rate
            clock.tick(10)

if __name__ == '__main__':
    game = SnakeGame()
    game.run()