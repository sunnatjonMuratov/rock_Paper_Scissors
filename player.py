import random


def get_user_choice():
    """
    Get the user's choice: Rock, Paper, or Scissors.
    """
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors(in lowercase): ").lower()
    return user_choice


def get_computer_choice():
    """
    Randomly generate the computer's choice: Rock, Paper, or Scissors.
    """
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
