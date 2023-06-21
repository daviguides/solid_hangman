"""This main module only loads and starts the app.
"""

from hangman import HangmanGameApp

if __name__ == "__main__":
    # Calls the app factory
    hg = HangmanGameApp.factory()
    # Defines if debug mode will be enabled
    hg.domain.debug = True
    # Starts the game
    hg.start()
