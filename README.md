# Rock, Paper, Scissors Game

This is a Python implementation of the classic Rock, Paper, Scissors game. The game allows the user to play against the computer in a command-line interface. The project is modular, with separate files handling different aspects of the game.

## Features

- **Command-line interface**: Simple and interactive text-based UI.
- **Modular Code**: The project is organized into multiple Python modules for better maintainability.
- **Score Tracking**: The game keeps track of the user's and computer's scores.
- **Replay Option**: The user can choose to play multiple rounds.
- **Extensible**: Easily add more features like a GUI or additional game options.

## Project Structure

rock_paper_scissors/                                                                                                           
├── init.py # Indicates that this directory is a package                                                                       
├── game.py # Main game logic (Entry point)                                                                                    
├── player.py # Handles user input and computer choice                                                                         
├── rules.py # Contains the logic for determining the winner                                                                   
├── utils.py # Utility functions (e.g., input validation, replay prompt)                                                       
└── test_game.py # Unit tests for the game logic                                                                               


## Prerequisites

- **Python 3.x**: Ensure you have Python installed. You can download it from the official [Python website](https://www.python.org/downloads/).

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/rock_paper_scissors.git
    cd rock_paper_scissors
    ```

2. **Install dependencies**:
   This project has no external dependencies, so you don't need to install any packages using `pip`.

3. **Run the game**:
    ```bash
    python game.py
    ```

4. **Run tests (Optional)**:
    If you'd like to run the unit tests, use the following command:
    ```bash
    python -m unittest test_game.py
    ```

## How to Play

- When prompted, enter your choice: `rock`, `paper`, or `scissors`.
- The computer will randomly select its choice.
- The program will determine the winner based on the classic rules:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock
- The game will display the result and the current score.
- You can play multiple rounds until you choose to quit.

## Future Improvements

- **Graphical User Interface (GUI)**: Implement a GUI using `tkinter` for a more interactive experience.
- **Additional Game Modes**: Add more choices, like "Lizard" and "Spock", or implement different game modes (e.g., best of 3).
- **Online Multiplayer**: Extend the game to support online multiplayer.

## License

This project is open-source and available under the MIT License.
