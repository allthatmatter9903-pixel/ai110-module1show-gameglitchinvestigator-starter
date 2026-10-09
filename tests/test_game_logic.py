import pytest
from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty

def test_check_guess_hints():
    assert check_guess(60, 50) == ("Lower", "📉 Go LOWER!")
    assert check_guess(40, 50) == ("Higher", "📈 Go HIGHER!")
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")

def test_parse_guess_valid_and_invalid():
    assert parse_guess("42") == (True, 42, None)
    
    is_valid, val, msg = parse_guess("3.14")
    assert not is_valid
    
    is_valid, val, msg = parse_guess("abc")
    assert not is_valid

def test_update_score_penalty():
    initial_score = 100
    new_score = update_score(initial_score, 1, 60, 50)
    assert new_score < initial_score
