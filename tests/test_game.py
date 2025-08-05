"""
Unit tests for the game components.
"""
import unittest
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from game.snake import Snake
from game.food import Food
from game.config import DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT
from utils.helpers import format_score


class TestSnake(unittest.TestCase):
    """Test the Snake class."""
    
    def setUp(self):
        self.snake = Snake()
    
    def test_initial_state(self):
        """Test snake initial state."""
        self.assertEqual(len(self.snake.body), 3)
        self.assertEqual(self.snake.direction, DIRECTION_RIGHT)
        self.assertEqual(self.snake.get_length(), 3)
    
    def test_movement(self):
        """Test snake movement."""
        initial_head = self.snake.get_head()
        self.snake.move()
        new_head = self.snake.get_head()
        self.assertNotEqual(initial_head, new_head)
        self.assertEqual(len(self.snake.body), 3)  # Should remain same length
    
    def test_direction_change(self):
        """Test direction changes."""
        self.snake.change_direction(DIRECTION_UP)
        self.assertEqual(self.snake.next_direction, DIRECTION_UP)
        
        # Test preventing reverse direction (when current direction is RIGHT, can't go LEFT)
        self.snake.change_direction(DIRECTION_LEFT)
        self.assertEqual(self.snake.next_direction, DIRECTION_UP)  # Should not change from UP
    
    def test_growth(self):
        """Test snake growth."""
        initial_length = self.snake.get_length()
        self.snake.grow(2)
        self.snake.move()
        self.assertEqual(self.snake.get_length(), initial_length + 1)
        self.snake.move()
        self.assertEqual(self.snake.get_length(), initial_length + 2)


class TestFood(unittest.TestCase):
    """Test the Food class."""
    
    def setUp(self):
        self.food = Food()
    
    def test_initial_position(self):
        """Test food has a valid initial position."""
        pos = self.food.get_position()
        self.assertIsInstance(pos, tuple)
        self.assertEqual(len(pos), 2)
        self.assertIsInstance(pos[0], int)
        self.assertIsInstance(pos[1], int)
    
    def test_spawn_away_from_snake(self):
        """Test food spawns away from snake."""
        snake_body = [(10, 10), (9, 10), (8, 10)]
        self.food.spawn_away_from_snake(snake_body)
        self.assertNotIn(self.food.get_position(), snake_body)


class TestHelpers(unittest.TestCase):
    """Test helper functions."""
    
    def test_format_score(self):
        """Test score formatting."""
        self.assertEqual(format_score(0), "000000")
        self.assertEqual(format_score(123), "000123")
        self.assertEqual(format_score(999999), "999999")


if __name__ == '__main__':
    unittest.main()
