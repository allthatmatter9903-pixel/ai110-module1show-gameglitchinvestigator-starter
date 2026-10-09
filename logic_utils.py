"""
Logic utility functions for Game Glitch Investigator.
Contains pure functions for difficulty ranges, guess parsing, scoring, and hint generation.
"""

def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """Returns (min, max) range for chosen difficulty."""
    if difficulty == "Easy":
        return 1, 20
    elif difficulty == "Hard":
        return 1, 500
    return 1, 100


def parse_guess(raw: str) -> tuple[bool, int | None, str | None]:
    """
    Parses string input to integer.
    Rejects floats/decimals and non-numeric characters gracefully.
    """
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            return False, None, "Please enter a whole integer, not a decimal."
        value = int(raw)
        return True, value, None
    except ValueError:
        return False, None, "That is not a valid number."


def check_guess(guess: int, secret: int) -> tuple[str, str]:
    """
    Compares numerical guess to secret number and returns (outcome, hint).
    Outcomes: "Win", "Lower", "Higher".
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    elif guess > secret:
        return "Lower", "📉 Go LOWER!"
    else:
        return "Higher", "📈 Go HIGHER!"


def update_score(current_score: int, attempts: int, guess: int, secret: int) -> int:
    """
    Deducts points per incorrect attempt.
    """
    penalty = 10
    return max(0, current_score - penalty)
