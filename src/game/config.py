"""
Game configuration constants and settings.
"""
from typing import Tuple

# Display settings
WINDOW_WIDTH: int = 800
WINDOW_HEIGHT: int = 600
WINDOW_TITLE: str = "Modern Snake Game"
FPS: int = 60

# Game grid settings
GRID_SIZE: int = 20
GRID_WIDTH: int = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT: int = WINDOW_HEIGHT // GRID_SIZE

# Game mechanics
INITIAL_SNAKE_LENGTH: int = 3
SNAKE_SPEED: int = 8  # Moves per second
SCORE_PER_FOOD: int = 10

# Directions
DIRECTION_UP: Tuple[int, int] = (0, -1)
DIRECTION_DOWN: Tuple[int, int] = (0, 1)
DIRECTION_LEFT: Tuple[int, int] = (-1, 0)
DIRECTION_RIGHT: Tuple[int, int] = (1, 0)

# Game states
STATE_MENU: str = "menu"
STATE_PLAYING: str = "playing"
STATE_PAUSED: str = "paused"
STATE_GAME_OVER: str = "game_over"

# High score file
HIGH_SCORE_FILE: str = "high_score.txt"
