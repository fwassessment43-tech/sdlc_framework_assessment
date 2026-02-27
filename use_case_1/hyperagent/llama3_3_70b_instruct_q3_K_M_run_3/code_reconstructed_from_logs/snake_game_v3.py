import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
SNAKE_COLOR = (255, 255, 255)
FOOD_COLOR = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font for the score
font = pygame.font.Font(None, 36)

# Set up the clock for a decent framerate
clock = pygame.time.Clock()

# Set up the snake and food
snake = [(200, 200), (220, 200), (240, 200)]
food = (400, 300)
direction = 'right'
score = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'
            elif event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'

    # Move the snake
    head = snake[-1]
    if direction == 'up':
        new_head = (head[0], head[1] - 20)
    elif direction == 'down':
        new_head = (head[0], head[1] + 20)
    elif direction == 'left':
        new_head = (head[0] - 20, head[1])
    elif direction == 'right':
        new_head = (head[0] + 20, head[1])
    snake.append(new_head)

    # Check for collisions with boundaries
    if (snake[-1][0] < 0 or snake[-1][0] >= WIDTH or
            snake[-1][1] < 0 or snake[-1][1] >= HEIGHT):
        print("Game over: collision with boundary")
        pygame.quit()
        sys.exit()

    # Check for collisions with body
    if snake[-1] in snake[:-1]:
        print("Game over: collision with body")
        pygame.quit()
        sys.exit()

    # Check for food consumption
    if snake[-1] == food:
        score += 1
        food = (random.randint(0, WIDTH - 20) // 20 * 20,
                random.randint(0, HEIGHT - 20) // 20 * 20)
    else:
        snake.pop(0)

    # Fill the screen with black
    screen.fill(BACKGROUND_COLOR)

    # Draw the snake and food
    for pos in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (pos[0], pos[1], 20, 20))
    pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], 20, 20))

    # Display the score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the framerate
    clock.tick(10)