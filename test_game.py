import unittest
from player import get_computer_choice
from rules import determine_winner


class TestRockPaperScissors(unittest.TestCase):

    def test_computer_choice(self):
        choice = get_computer_choice()
        self.assertIn(choice, ["rock", "paper", "scissors"])

    def test_winner_determination(self):
        self.assertEqual(determine_winner("rock", "scissors"), "You win!")
        self.assertEqual(determine_winner("scissors", "rock"), "You lose!")
        self.assertEqual(determine_winner("paper", "rock"), "You win!")
        self.assertEqual(determine_winner("rock", "rock"), "It's a tie!")


if __name__ == '__main__':
    unittest.main()
