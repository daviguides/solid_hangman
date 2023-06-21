"""This package contains one or more factories,
following the pattern that assembles several classes to run an application.
"""

# Imports the HangmanGame
from .controller import HangmanGame


# This class is a factory pattern that builds the terminal hangman game
class HangmanGameTerminalFactory:
    @classmethod
    def factory(cls):
        # imports the concrete classes to build the terminal game
        from .views import PromptChoicesCanvas, HangCanvas, WonCanvas, HangedCanvas

        # uses the word loader from files
        from .common import FileWordLoader

        # loads the singleton domain of the game
        from .domain import domain

        # returns the fully assembled game
        return HangmanGame(
            # loads the singleton domain
            domain=domain,
            # uses the text file word loader
            file_loader=FileWordLoader.factory(),
            # loads the difficulty selection screen for the terminal
            prompt_choices=PromptChoicesCanvas.factory(
                question="Choose a level", options=["Easy", "Hard"]
            ),
            # loads the hangman screen for the terminal
            hang_canvas=HangCanvas.factory(),
            # loads the victory screen for the terminal
            won_screen=WonCanvas.factory(),
            # loads the hanged (loss) screen for the terminal
            hanged_canvas=HangedCanvas.factory(),
        )
