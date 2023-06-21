"""This package contains the abstract base class for the Hangman game
with the expected contract signature.
"""

from abc import ABC

# Imports abstract classes, not concrete classes,
# because the game can have multiple implementations (e.g., terminal, web)
from .common import Canvas, WordLoader
from .domain import HangmanDomain

class HangmanGameBase(ABC):
    """This abstract class defines the expected contract signature
    for a Hangman game implementation.
    """

    def __init__(self,
            # Game model
            domain: HangmanDomain,
            # Word loader
            file_loader: WordLoader,
            # Difficulty selection screen
            prompt_choices: Canvas,
            # Hangman screen
            hang_canvas: Canvas,
            # Congratulations screen
            won_screen: Canvas,
            # Hanged man (loss) screen
            hanged_canvas: Canvas):

        # Below, the class signature is set to their respective properties
        self.domain: HangmanDomain = domain
        self.prompt_choices: WordLoader = prompt_choices
        self.load_word: Canvas = file_loader
        self.hang_canvas: Canvas = hang_canvas
        self.won_screen: Canvas = won_screen
        self.hanged_canvas: Canvas = hanged_canvas
