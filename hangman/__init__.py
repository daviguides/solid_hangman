# The version of an app should be defined in its main package
__author__ = "Davi Luiz Guides"
__version__ = "0.1.0"

# Shortcut to the main class of this library
from .factory import HangmanGameTerminalFactory

# A simple facade for the application pointing to the factory
class HangmanGameApp:
    @classmethod
    def factory(cls):
        return HangmanGameTerminalFactory.factory()