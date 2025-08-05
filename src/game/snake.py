"""
Snake entity implementation.
"""
from typing import List, Tuple
from src.game.config import (
    DIRECTION_RIGHT, DIRECTION_LEFT, DIRECTION_UP, DIRECTION_DOWN,
    INITIAL_SNAKE_LENGTH, GRID_WIDTH, GRID_HEIGHT
)


class Snake:
    """Represents the snake in the game."""
    
    def __init__(self) -> None:
        """Initialize the snake with default position and direction."""
        self.reset()
    
    def reset(self) -> None:
        """Reset the snake to initial state."""
        # Start snake in the middle of the screen
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        
        # Initialize snake body (head first)
        self.body: List[Tuple[int, int]] = []
        for i in range(INITIAL_SNAKE_LENGTH):
            self.body.append((start_x - i, start_y))
        
        self.direction: Tuple[int, int] = DIRECTION_RIGHT
        self.next_direction: Tuple[int, int] = DIRECTION_RIGHT
        self.grow_pending: int = 0
    
    def get_head(self) -> Tuple[int, int]:
        """Get the head position of the snake."""
        return self.body[0]
    
    def change_direction(self, new_direction: Tuple[int, int]) -> None:
        """Change the snake's direction if it's valid."""
        # Prevent reversing into itself
        current_dir = self.direction
        if (new_direction[0] * -1, new_direction[1] * -1) != current_dir:
            self.next_direction = new_direction
    
    def move(self) -> None:
        """Move the snake one step forward."""
        # Update direction
        self.direction = self.next_direction
        
        # Calculate new head position
        head_x, head_y = self.get_head()
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Add new head
        self.body.insert(0, new_head)
        
        # Remove tail unless growing
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()
    
    def grow(self, segments: int = 1) -> None:
        """Make the snake grow by the specified number of segments."""
        self.grow_pending += segments
    
    def check_wall_collision(self) -> bool:
        """Check if the snake has collided with the walls."""
        head_x, head_y = self.get_head()
        return (head_x < 0 or head_x >= GRID_WIDTH or 
                head_y < 0 or head_y >= GRID_HEIGHT)
    
    def check_self_collision(self) -> bool:
        """Check if the snake has collided with itself."""
        head = self.get_head()
        return head in self.body[1:]  # Check if head is in the rest of the body
    
    def get_length(self) -> int:
        """Get the current length of the snake."""
        return len(self.body)
