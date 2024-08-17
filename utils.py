def ask_to_play_again():
    """
    Ask the user if they want to play again.
    """
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    return play_again == "yes"
