"""
Utility helper functions.
"""
import os
from typing import Optional
from src.game.config import HIGH_SCORE_FILE


def load_high_score() -> int:
    """Load the high score from file."""
    try:
        if os.path.exists(HIGH_SCORE_FILE):
            with open(HIGH_SCORE_FILE, 'r') as f:
                return int(f.read().strip())
    except (ValueError, IOError):
        pass
    return 0


def save_high_score(score: int) -> None:
    """Save the high score to file."""
    try:
        with open(HIGH_SCORE_FILE, 'w') as f:
            f.write(str(score))
    except IOError:
        pass  # Fail silently if we can't save


def format_score(score: int) -> str:
    """Format score with leading zeros."""
    return f"{score:06d}"


def clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamp a value between min and max."""
    return max(min_val, min(value, max_val))
