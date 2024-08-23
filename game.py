from player import get_user_choice, get_computer_choice
from rules import determine_winner
from utils import ask_to_play_again


def play_game():
    """
    Main function to play the Rock, Paper, Scissors game
    """
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"\nScore: You {user_score} - {computer_score} Computer")

        if not ask_to_play_again():
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
