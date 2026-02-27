'''
game.py
This module orchestrates the main loop, event handling, rendering,
scorekeeping, collision checks and restart logic.  An instruction
overlay is now displayed during normal gameplay to satisfy the
user‑interface requirement of providing clear, interactive
instructions.  The overlay reads: “Use arrow keys to move. Eat
food to grow.”  The existing “Press R to restart” message
remains visible after game over.
'''
import pygame
import sys
from constants import SCREEN_SIZE, COLORS, FPS, DIRECTIONS, CELL_SIZE
from snake import Snake
from food import Food
class Game:
    """
    Main game controller.
    Methods
    -------
    reset()
        Restart the game to its initial state.
    handle_events()
        Process keyboard input.
    update()
        Move snake, handle collisions, update score.
    draw_grid()
        Render the grid background.
    draw()
        Draw all game objects and UI.
    run()
        Start the main game loop.
    """
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.reset()
    def reset(self):
        """
        Reset all game variables to start a new game.
        """
        self.snake = Snake(initial_pos=(5, 5))
        self.food = Food(self.snake.body)
        self.score = 0
        self.game_over = False
    def handle_events(self):
        """
        Handle keyboard input and quit events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if not self.game_over:
                    if event.key == pygame.K_UP:
                        self.snake.set_direction(DIRECTIONS['UP'])
                    elif event.key == pygame.K_DOWN:
                        self.snake.set_direction(DIRECTIONS['DOWN'])
                    elif event.key == pygame.K_LEFT:
                        self.snake.set_direction(DIRECTIONS['LEFT'])
                    elif event.key == pygame.K_RIGHT:
                        self.snake.set_direction(DIRECTIONS['RIGHT'])
                else:
                    if event.key == pygame.K_r:
                        self.reset()
    def update(self):
        """
        Update game state: move snake, check collisions,
        handle food consumption and game over conditions.
        """
        if self.game_over:
            return
        self.snake.move()
        # Collision with boundaries
        if self.snake.collides_with_boundary():
            self.game_over = True
            return
        # Collision with self
        if self.snake.collides_with_self():
            self.game_over = True
            return
        # If no food left (board full), trigger game over
        if self.food.position is None:
            self.game_over = True
            return
        # Food consumption
        if self.snake.head() == self.food.position:
            self.score += 1
            self.snake.grow()
            self.food.generate(self.snake.body)
    def draw_grid(self):
        """
        Draw a simple grid background.
        """
        self.screen.fill(COLORS['BLACK'])
        # Draw vertical grid lines
        for x in range(0, SCREEN_SIZE, CELL_SIZE):
            pygame.draw.line(self.screen, COLORS['GRAY'], (x, 0), (x, SCREEN_SIZE))
        # Draw horizontal grid lines
        for y in range(0, SCREEN_SIZE, CELL_SIZE):
            pygame.draw.line(self.screen, COLORS['GRAY'], (0, y), (SCREEN_SIZE, y))
    def draw(self):
        """
        Render all game elements and UI text.
        """
        self.draw_grid()
        # Draw food
        if self.food.position is not None:
            food_rect = pygame.Rect(
                self.food.position[0] * CELL_SIZE,
                self.food.position[1] * CELL_SIZE,
                CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, COLORS['RED'], food_rect)
        # Draw snake
        for segment in self.snake.body:
            seg_rect = pygame.Rect(
                segment[0] * CELL_SIZE,
                segment[1] * CELL_SIZE,
                CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, COLORS['GREEN'], seg_rect)
        # Score display
        score_surf = self.font.render(f"Score: {self.score}", True, COLORS['WHITE'])
        self.screen.blit(score_surf, (10, 10))
        # Instruction text during normal play
        if not self.game_over:
            instr_surf = self.font.render(
                "Use arrow keys to move. Eat food to grow.", True, COLORS['WHITE'])
            self.screen.blit(instr_surf, (10, SCREEN_SIZE - 30))
        # Game over overlay
        if self.game_over:
            overlay = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))  # semi-transparent black
            self.screen.blit(overlay, (0, 0))
            msg = self.font.render("GAME OVER", True, COLORS['WHITE'])
            msg_rect = msg.get_rect(center=(SCREEN_SIZE // 2, SCREEN_SIZE // 2 - 20))
            self.screen.blit(msg, msg_rect)
            restart_msg = self.font.render("Press R to Restart", True, COLORS['WHITE'])
            restart_rect = restart_msg.get_rect(center=(SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 20))
            self.screen.blit(restart_msg, restart_rect)
        pygame.display.flip()
    def run(self):
        """
        Main game loop.
        """
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)