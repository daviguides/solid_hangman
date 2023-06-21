import os
from abc import ABC

class Canvas(ABC):
    """Abstract class representing a canvas,
    e.g., a canvas for terminal usage or a graphical window.
    """
    pass

class TerminalCanvas(ABC):
    """This abstract class implements some common properties
    and private functions that are used by the game screens.
    """
    def __init__(self, domain):
        self.domain = domain
        # Constant with the character used for horizontal lines ====
        self.LINE_CHAR = "="
        # Constant with the character used for vertical lines ||
        self.WALL_CHAR = "||"

    @classmethod
    def factory(cls):
        from hangman.domain import domain
        return cls(domain=domain)
    
    def _print_interline(self, value):
        # Prints a line with a blank line above and below
        print(f'\n{value} \n')

    def _print_line(self, value):
        # Prints a single line
        print(f"{self.WALL_CHAR}  {value}")
    
    def _print_lines(self, values):
        # Prints a sequence of lines
        for value in values:
            self._print_line(value)

    # Function that clears the screen
    def _clear_screen(self):
        # Checks if it's a Unix-based system (Linux, macOS)
        if os.name == 'posix':
            # If yes, runs the corresponding clear command
            os.system('clear')
        else:
            # Otherwise, runs the clear command for Windows
            os.system('cls')