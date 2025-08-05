"""
Game engine implementation.
"""
import pygame
from typing import Optional
from src.game.snake import Snake
from src.game.food import Food
from src.ui.colors import BLACK, SNAKE_HEAD, SNAKE_BODY, FOOD_COLOR, GRID_LINE, TEXT_PRIMARY, TEXT_SECONDARY
from src.utils.helpers import load_high_score, save_high_score, format_score
from src.game.config import (
    STATE_GAME_OVER, STATE_MENU, STATE_PLAYING, STATE_PAUSED,
    GRID_SIZE, SCORE_PER_FOOD, DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT,
    SNAKE_SPEED, FPS
)


class GameEngine:
    """Handles the main game mechanics and state transitions."""

    def __init__(self, window: pygame.Surface) -> None:
        self.window = window
        self.state = STATE_PLAYING  # Start directly in playing mode
        self.snake = Snake()
        self.food = Food()
        self.food.spawn_away_from_snake(self.snake.body)
        self.score = 0
        self.high_score = load_high_score()
        
        # Game timing
        self.move_timer = 0
        self.move_delay = FPS // SNAKE_SPEED
        
        # Font for UI
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.large_font = pygame.font.Font(None, 72)

    def update(self) -> None:
        """Update the game state."""
        if self.state == STATE_PLAYING:
            self.handle_input()
            
            # Control snake movement speed
            self.move_timer += 1
            if self.move_timer >= self.move_delay:
                self.move_timer = 0
                self.snake.move()

                # Check collisions
                if self.snake.check_wall_collision() or self.snake.check_self_collision():
                    self.state = STATE_GAME_OVER
                    if self.score > self.high_score:
                        self.high_score = self.score
                        save_high_score(self.score)
                        
                # Check food collision
                if self.snake.get_head() == self.food.get_position():
                    self.snake.grow()
                    self.score += SCORE_PER_FOOD
                    self.food.spawn_away_from_snake(self.snake.body)
        
        elif self.state == STATE_GAME_OVER:
            self.handle_game_over_input()

    def handle_input(self) -> None:
        """Handle user input to control the game."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.snake.change_direction(DIRECTION_UP)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.snake.change_direction(DIRECTION_DOWN)
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.snake.change_direction(DIRECTION_LEFT)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.snake.change_direction(DIRECTION_RIGHT)
    
    def handle_game_over_input(self) -> None:
        """Handle input when game is over."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
            self.reset_game()

    def render(self) -> None:
        """Render the current game state to the window."""
        self.window.fill(BLACK)  # Background
        
        if self.state == STATE_PLAYING:
            self.draw_grid()
            self.draw_snake()
            self.draw_food()
            self.draw_hud()
        elif self.state == STATE_GAME_OVER:
            self.draw_grid()
            self.draw_snake()
            self.draw_food()
            self.draw_game_over_screen()

    def draw_grid(self) -> None:
        """Draw the game grid."""
        for x in range(0, self.window.get_width(), GRID_SIZE):
            for y in range(0, self.window.get_height(), GRID_SIZE):
                rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(self.window, GRID_LINE, rect, 1)

    def draw_snake(self) -> None:
        """Draw the snake on the screen."""
        for segment in self.snake.body:
            rect = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(self.window, SNAKE_HEAD if segment == self.snake.get_head() else SNAKE_BODY, rect)

    def draw_food(self) -> None:
        """Draw the food on the screen."""
        food_pos = self.food.get_position()
        rect = pygame.Rect(food_pos[0] * GRID_SIZE, food_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(self.window, FOOD_COLOR, rect)

    def draw_hud(self) -> None:
        """Draw the heads-up display with score and high score."""
        score_text = self.font.render(f"Score: {format_score(self.score)}", True, TEXT_PRIMARY)
        high_score_text = self.font.render(f"High Score: {format_score(self.high_score)}", True, TEXT_SECONDARY)
        length_text = self.font.render(f"Length: {self.snake.get_length()}", True, TEXT_SECONDARY)
        
        self.window.blit(score_text, (10, 10))
        self.window.blit(high_score_text, (10, 50))
        self.window.blit(length_text, (10, 90))
    
    def draw_game_over_screen(self) -> None:
        """Draw the game over screen."""
        # Semi-transparent overlay
        overlay = pygame.Surface((self.window.get_width(), self.window.get_height()))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.window.blit(overlay, (0, 0))
        
        # Game over text
        game_over_text = self.large_font.render("GAME OVER", True, TEXT_PRIMARY)
        final_score_text = self.font.render(f"Final Score: {format_score(self.score)}", True, TEXT_SECONDARY)
        restart_text = self.font.render("Press SPACE to play again", True, TEXT_SECONDARY)
        
        # Center the text
        game_over_rect = game_over_text.get_rect(center=(self.window.get_width()//2, self.window.get_height()//2 - 50))
        final_score_rect = final_score_text.get_rect(center=(self.window.get_width()//2, self.window.get_height()//2))
        restart_rect = restart_text.get_rect(center=(self.window.get_width()//2, self.window.get_height()//2 + 50))
        
        self.window.blit(game_over_text, game_over_rect)
        self.window.blit(final_score_text, final_score_rect)
        self.window.blit(restart_text, restart_rect)

    def reset_game(self) -> None:
        """Reset the game to initial state."""
        self.snake.reset()
        self.food.spawn_away_from_snake(self.snake.body)
        self.score = 0
        self.move_timer = 0
        self.state = STATE_PLAYING
