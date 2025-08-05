"""
Main game loop and execution.
"""
import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from src.game.config import FPS, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE
from src.game.engine import GameEngine


def run_game():
    """Run the game loop."""
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    clock = pygame.time.Clock()
    game_engine = GameEngine(window)
    
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        # Update and render game
        game_engine.update()
        game_engine.render()

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    run_game()
