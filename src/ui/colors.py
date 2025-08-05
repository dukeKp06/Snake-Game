"""
Color definitions for the game UI.
"""
from typing import Tuple

# Type alias for RGB color
Color = Tuple[int, int, int]

# Background colors
BLACK: Color = (0, 0, 0)
WHITE: Color = (255, 255, 255)
DARK_GRAY: Color = (64, 64, 64)
LIGHT_GRAY: Color = (128, 128, 128)

# Game colors
SNAKE_HEAD: Color = (0, 200, 0)
SNAKE_BODY: Color = (0, 150, 0)
SNAKE_OUTLINE: Color = (0, 100, 0)
FOOD_COLOR: Color = (255, 50, 50)
FOOD_OUTLINE: Color = (200, 0, 0)

# UI colors
TEXT_PRIMARY: Color = (255, 255, 255)
TEXT_SECONDARY: Color = (200, 200, 200)
BUTTON_COLOR: Color = (70, 130, 180)
BUTTON_HOVER: Color = (100, 149, 237)
ACCENT_COLOR: Color = (255, 215, 0)

# Grid
GRID_LINE: Color = (40, 40, 40)
