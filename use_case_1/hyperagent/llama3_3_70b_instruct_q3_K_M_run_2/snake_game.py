import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 600
HEIGHT = 600
BLOCK_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the clock
clock = pygame.time.Clock()

class SnakeGame:
    def __init__(self):
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = 'RIGHT'
        self.food = self.generate_food()
        self.score = 0
        self.high_score = 0

    def generate_food(self):
        while True:
            food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE, 
                     random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
            if food not in self.snake:
                return food

    def draw_snake(self):
        for pos in self.snake:
            pygame.draw.rect(win, WHITE, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

    def draw_food(self):
        pygame.draw.rect(win, RED, (self.food[0], self.food[1], BLOCK_SIZE, BLOCK_SIZE))

    def move_snake(self):
        head = self.snake[-1]
        if self.direction == 'RIGHT':
            new_head = (head[0] + BLOCK_SIZE, head[1])
        elif self.direction == 'LEFT':
            new_head = (head[0] - BLOCK_SIZE, head[1])
        elif self.direction == 'UP':
            new_head = (head[0], head[1] - BLOCK_SIZE)
        elif self.direction == 'DOWN':
            new_head = (head[0], head[1] + BLOCK_SIZE)

        self.snake.append(new_head)
        if self.food == new_head:
            self.score += 1
            self.food = self.generate_food()
        else:
            self.snake.pop(0)

    def check_collision(self):
        head = self.snake[-1]
        if (head[0] < 0 or head[0] >= WIDTH or 
            head[1] < 0 or head[1] >= HEIGHT or 
            head in self.snake[:-1]):
            if self.score > self.high_score:
                self.high_score = self.score
            return True
        return False

    def draw_score(self):
        text = font.render(f'Score: {self.score}', True, WHITE)
        win.blit(text, (10, 10))

    def draw_high_score(self):
        text = font.render(f'High Score: {self.high_score}', True, WHITE)
        win.blit(text, (10, 40))

def main():
    game = SnakeGame()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and game.direction != 'DOWN':
                    game.direction = 'UP'
                elif event.key == pygame.K_DOWN and game.direction != 'UP':
                    game.direction = 'DOWN'
                elif event.key == pygame.K_LEFT and game.direction != 'RIGHT':
                    game.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and game.direction != 'LEFT':
                    game.direction = 'RIGHT'

        win.fill(BLACK)
        game.move_snake()
        if game.check_collision():
            text = font.render('Game Over', True, WHITE)
            win.blit(text, (WIDTH // 2 - 50, HEIGHT // 2))
            pygame.display.update()
            pygame.time.wait(2000)
            break
        game.draw_snake()
        game.draw_food()
        game.draw_score()
        game.draw_high_score()
        if game.score % 5 == 0 and game.score != 0:
            clock.tick(15)
        else:
            clock.tick(10)
        pygame.display.update()

if __name__ == '__main__':
    main()
