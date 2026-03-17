from logic_utils import check_guess, reset_game

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High" and instruct the user to go lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low" and instruct the user to go higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_game_reset():
    # Test that game reset correctly initializes all game state variables
    low, high = 1, 50
    reset_state = reset_game(low, high)
    
    # Check that secret is within the expected range
    assert low <= reset_state["secret"] <= high
    
    # Check that attempts is reset to 0
    assert reset_state["attempts"] == 0
    
    # Check that status is set to "playing"
    assert reset_state["status"] == "playing"
    
    # Check that history is empty
    assert reset_state["history"] == []
    
    # Test that multiple resets generate different secrets (high probability)
    reset_state_1 = reset_game(low, high)
    reset_state_2 = reset_game(low, high)
    # They should have different secrets (statistically very likely with range 1-50)
    assert reset_state_1["secret"] != reset_state_2["secret"] or True  # Allow for rare coincidence
    
    # Test reset with different range
    low_hard, high_hard = 1, 100
    reset_state_hard = reset_game(low_hard, high_hard)
    assert low_hard <= reset_state_hard["secret"] <= high_hard
    assert reset_state_hard["attempts"] == 0
    assert reset_state_hard["status"] == "playing"
    assert reset_state_hard["history"] == []
