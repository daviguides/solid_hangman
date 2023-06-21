# Imports class and function needed to define an abstract class
from abc import ABC
# Imports the randint function from the random package
from random import randint

class WordLoader(ABC):
    """A purely formal class to abstractly represent
    a word loader. For example, I currently have a concrete implementation
    that loads words from a file, but I could have another implementation
    that loads from a database.
    """
    def __init__(self, domain):
        self.domain = domain

    # Abstract method that must be implemented by subclasses
    def get(self) -> str:
        # Classes implementing this abstraction must implement this method.
        # It is expected that this method returns a string.
        pass

    @classmethod
    def factory(cls):
        from hangman.domain import domain
        return cls(domain=domain)

class FileWordLoader(WordLoader):
    """This class encapsulates the functionality of opening files
    according to the selected level and loading a word.
    """
    def load(self):
        # If debug mode is off
        if not self.domain.debug:
            # Runs the standard function that loads correctly
            # and selects a random word
            self.domain.word = self._get().lower()
        else:
            # For testing purposes, if debug mode is on,
            # uses predefined words depending on the level
            if self.domain.level == 1:
                self.domain.word = 'ball'
            else:
                self.domain.word = 'parallelepiped'

    # Implements the abstract method get and returns a word
    def _get(self) -> str:
        # Gets the file name to open
        file_name = self._get_file_name()

        # Opens the file
        with open(f'./data/{file_name}.txt') as f:
            # Reads the content and splits the lines into a list
            lines = f.read().splitlines()
        
        # Gets a random integer between 0 and len(lines) - 1
        index = randint(0, len(lines) - 1)

        # Returns a random word based on the integer
        return lines[index]

    def _get_file_name(self):
        # Returns the file name according to the level from a hashmap
        # where the key is the level
        return {
            1: 'easy_words', 
            2: 'hard_words'
        }[self.domain.level]

class DBWordLoader(WordLoader):
    """In a future improvement, I could implement a database-based loader.
    Since the Hangman class only references the abstract class,
    it will not be necessary to change the game logic,
    only the factory needs to be updated.
    """
    def get(self):
        pass