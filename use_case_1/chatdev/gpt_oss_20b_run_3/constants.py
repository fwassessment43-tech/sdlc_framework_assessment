'''
constants.py
'''
# Grid configuration
GRID_SIZE = 10          # 10x10 grid
CELL_SIZE = 40          # each cell is 40x40 pixels
SCREEN_SIZE = GRID_SIZE * CELL_SIZE
# Game speed
FPS = 10  # frames per second (controls snake speed)
# Colors (RGB)
COLORS = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'GREEN': (0, 255, 0),
    'DARK_GREEN': (0, 155, 0),
    'RED': (255, 0, 0),
    'GRAY': (100, 100, 100),
}
# Directions
DIRECTIONS = {
    'UP': (0, -1),
    'DOWN': (0, 1),
    'LEFT': (-1, 0),
    'RIGHT': (1, 0),
}