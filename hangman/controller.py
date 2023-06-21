"""This package contains the game controller, which is the heart of the application,
responsible for executing the commands that make the game happen.
"""

# Imports the abstract base class that defines the game contract
from .base import HangmanGameBase

class HangmanGame(HangmanGameBase):
    """This class implements the controller pattern that connects
    the domain and view of the application.
    This class itself is mostly unaware of the internal structure of the domain
    and the views — it only calls their main functions.
    """

    # Main function that starts the game
    def start(self):
        # Displays the level selection screen
        self.prompt_choices.show()

        # Loads a word based on the selected level
        self.load_word.load()

        # Starts the main game loop
        if self.hang_canvas.show():
            # If player wins, shows the victory animation screen
            self.won_screen.show()
        else:
            # Otherwise, shows the hanged man animation (losing screen)
            self.hanged_canvas.show()