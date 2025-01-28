import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO

# Add the main directory to the Python module search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine import load_challenges, validate_command, start_game  # Import from engine.py
from scoring import update_score

class TestLinuxLearningGame(unittest.TestCase):

    @patch('builtins.open')
    def test_load_challenges(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = '{"challenges": [{"id": 1, "description": "Test Challenge"}]}'
        challenges = load_challenges('beginner')
        self.assertEqual(len(challenges), 1)
        self.assertEqual(challenges[0]['id'], 1)

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_load_challenges_file_not_found(self, mock_open):
        challenges = load_challenges('beginner')
        self.assertEqual(challenges, [])

    @patch('subprocess.check_output')
    def test_validate_command_valid(self, mock_check_output):
        mock_check_output.return_value = 'expected_output'
        user_input = 'echo Hello'
        solution = 'expected_output'
        result = validate_command(user_input, solution)
        self.assertTrue(result)

    @patch('subprocess.check_output')
    def test_validate_command_invalid(self, mock_check_output):
        mock_check_output.return_value = 'wrong_output'
        user_input = 'echo Hello'
        solution = 'expected_output'
        result = validate_command(user_input, solution)
        self.assertFalse(result)

    @patch('subprocess.check_output', side_effect=Exception)
    def test_validate_command_error(self, mock_check_output):
        user_input = 'invalid_command'
        solution = 'expected_output'
        result = validate_command(user_input, solution)
        self.assertFalse(result)

    @patch('builtins.input', side_effect=['1', 'echo Hello'])
    @patch('builtins.print')
    @patch('engine.load_challenges')
    def test_start_game(self, mock_load_challenges, mock_print, mock_input):
        challenge_data = {'id': 1, 'description': 'Test Challenge', 'solution': 'expected_output', 'hints': ['Use echo']}
        mock_load_challenges.return_value = [challenge_data]
        start_game()
        mock_print.assert_any_call('Select Difficulty Level:')
        mock_print.assert_any_call('1. Beginner')

    @patch('builtins.input', side_effect=['4'])
    @patch('builtins.print')
    def test_start_game_invalid_level(self, mock_print, mock_input):
        start_game()
        mock_print.assert_any_call('Invalid level choice! Returning to main menu...')

    @patch('engine.update_score')
    def test_update_score(self, mock_update_score):
        update_score(50)
        mock_update_score.assert_called_with(50)

    @patch('builtins.input', side_effect=['hint', 'echo Hello', 'hint', 'echo Hello'])
    @patch('builtins.print')
    def test_hint_usage(self, mock_print, mock_input):
        score = 20
        hints_used = 0
        while True:
            user_input = input("Enter command (or 'hint'): ")
            if user_input.lower() == 'hint' and hints_used < 1:
                hints_used += 1
                score -= 5
            elif validate_command(user_input, 'expected_output'):
                score += 10
                break
        self.assertEqual(score, 25)

    @patch('builtins.input', side_effect=['echo Hello'])
    @patch('builtins.print')
    def test_challenge_completion(self, mock_print, mock_input):
        challenge_data = {'id': 1, 'description': 'Test Challenge', 'solution': 'expected_output', 'hints': ['Use echo']}
        challenges = [challenge_data]
        challenge = challenges[0]
        self.assertEqual(challenge['id'], 1)
        mock_print.assert_any_call("Correct! +10 points")

    @patch('builtins.input', side_effect=['echo Hello'])
    @patch('builtins.print')
    @patch('engine.load_challenges')
    def test_game_loop_display_challenge(self, mock_load_challenges, mock_print, mock_input):
        challenge_data = {'id': 1, 'description': 'Test Challenge', 'solution': 'expected_output', 'hints': ['Use echo']}
        mock_load_challenges.return_value = [challenge_data]
        start_game()
        mock_print.assert_any_call('Challenge 1:')
        mock_print.assert_any_call('Test Challenge')


if __name__ == '__main__':
    unittest.main()

