'''
game.py
Manages the main game loop, event handling, updates, and rendering.
'''
import pygame
import sys
from constants import GameConfig
from board import Board
from snake import Snake, UP, DOWN, LEFT, RIGHT
from food import Food
class Game:
    def __init__(self):
        pygame.init()
        self.config = GameConfig()
        self.screen = pygame.display.set_mode((self.config.WIDTH, self.config.HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.board = Board(self.config)
        self.reset_game()
    def reset_game(self):
        '''Initialize or reset all game components.'''
        start_pos = (self.config.GRID_SIZE // 2, self.config.GRID_SIZE // 2)
        self.snake = Snake(start_pos)
        self.food = Food(self.config, self.snake)
        self.score = 0
        self.game_over = False
        self.last_move_time = 0
        self.move_interval = 1000 // self.config.FPS
        self.collision_flash_start = 0
        self.food_flash_start = 0
    def handle_events(self):
        '''Process user input and system events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(RIGHT)
                elif event.key == pygame.K_r and self.game_over:
                    self.reset_game()
    def update(self):
        '''Update game state: move snake, handle collisions, and food consumption.'''
        if self.game_over:
            return
        now = pygame.time.get_ticks()
        if now - self.last_move_time > self.move_interval:
            self.last_move_time = now
            self.snake.move()
            # Collision checks
            if self.snake.collides_with_wall(self.config) or self.snake.collides_with_self():
                self.game_over = True
                self.collision_flash_start = now
                return
            # Food consumption
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.score += 1
                self.food.reposition()
                self.food_flash_start = now
                self.food.start_flash(now)
    def render_text(self, text: str, pos: tuple, color: tuple = None):
        '''Utility to render a text surface onto the screen.'''
        if color is None:
            color = self.config.TEXT
        text_surf = self.font.render(text, True, color)
        self.screen.blit(text_surf, pos)
    def render(self):
        '''Draw all game elements onto the screen with animations.'''
        now = pygame.time.get_ticks()
        # Draw board background and grid
        self.board.draw(self.screen)
        # Draw food with possible flash
        self.food.draw(self.screen, now)
        # Draw snake
        # Interpolate head position for smooth movement
        head_grid = self.snake.body[0]
        prev_head_grid = self.snake.prev_head_pos
        elapsed_since_move = now - self.last_move_time
        fraction = min(1.0, elapsed_since_move / self.move_interval)
        head_px_start = (prev_head_grid[0] * self.config.CELL_SIZE,
                         prev_head_grid[1] * self.config.CELL_SIZE)
        head_px_end = (head_grid[0] * self.config.CELL_SIZE,
                       head_grid[1] * self.config.CELL_SIZE)
        interp_px = (head_px_start[0] + fraction * (head_px_end[0] - head_px_start[0]),
                     head_px_start[1] + fraction * (head_px_end[1] - head_px_start[1]))
        # Draw body segments (excluding head)
        for idx, (x, y) in enumerate(self.snake.body[1:]):
            rect = pygame.Rect(x * self.config.CELL_SIZE, y * self.config.CELL_SIZE,
                               self.config.CELL_SIZE, self.config.CELL_SIZE)
            pygame.draw.rect(self.screen, self.config.SNAKE_BODY, rect)
        # Draw head with possible collision flash
        head_color = self.config.SNAKE_HEAD
        if now - self.collision_flash_start < self.config.FLASH_DURATION:
            head_color = self.config.FLASH_HEAD
        head_rect = pygame.Rect(interp_px[0], interp_px[1],
                                self.config.CELL_SIZE, self.config.CELL_SIZE)
        pygame.draw.rect(self.screen, head_color, head_rect)
        # Display score
        self.render_text(f"Score: {self.score}", (10, 10))
        # Display instructions when game is not over
        if not self.game_over:
            self.render_text("Press arrow keys to move.", (10, 50))
            self.render_text("Press R to restart after Game Over.", (10, 80))
        else:
            # Game over message
            self.render_text("GAME OVER", (self.config.WIDTH // 4, self.config.HEIGHT // 3), (255, 0, 0))
            self.render_text("Press R to Restart", (self.config.WIDTH // 6, self.config.HEIGHT // 2))
        pygame.display.flip()
    def run(self):
        '''Main loop: event handling, updating, rendering.'''
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)  # Cap at 60 FPS for input responsiveness