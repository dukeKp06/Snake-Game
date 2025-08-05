"""
Food entity implementation.
"""
import random
from typing import Tuple, List
from src.game.config import GRID_WIDTH, GRID_HEIGHT


class Food:
    """Represents food in the game."""
    
    def __init__(self) -> None:
        """Initialize food at a random position."""
        self.position: Tuple[int, int] = (0, 0)
        self.spawn_random()
    
    def spawn_random(self) -> None:
        """Spawn food at a random position."""
        self.position = (
            random.randint(0, GRID_WIDTH - 1),
            random.randint(0, GRID_HEIGHT - 1)
        )
    
    def spawn_away_from_snake(self, snake_body: List[Tuple[int, int]]) -> None:
        """Spawn food at a position not occupied by the snake."""
        max_attempts = 100  # Prevent infinite loop
        attempts = 0
        
        while attempts < max_attempts:
            self.spawn_random()
            if self.position not in snake_body:
                break
            attempts += 1
        
        # If we couldn't find a free spot (very unlikely), just use the current position
    
    def get_position(self) -> Tuple[int, int]:
        """Get the current position of the food."""
        return self.position
