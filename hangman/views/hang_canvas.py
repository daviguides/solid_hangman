from hangman.common import TerminalCanvas

class HangCanvas(TerminalCanvas):
    # Main function
    def show(self):
        while True:
            # Displays the main hangman screen
            self.draw()

            # If the player reaches the maximum number of mistakes or discovers the word,
            # the game loop is interrupted
            if self.domain.error_count == 6 \
                or self.domain.secret == self.domain.word:
                break

            # Otherwise, opens the input for the player to guess another letter
            self._print_input()
        return self.domain.secret == self.domain.word

    # Draws the screen
    def draw(self):
        # Gets the secret word
        self._get_secret()

        # Prints the top of the gallows
        print(f"||===:===\n||   :")
        # Prints the head if there is at least one mistake
        head = " O" if self.domain.error_count >= 1 else ""
        self._print_line(head)

        # Prints the body parts based on the number of mistakes
        body_parts = {
            0:"\n||",
            1:"\n||",
            2:" | \n||", # == 2
            3:"\| \n||", # == 3
            4:"\|/\n||", # >= 4
            5:"\|/\n||  /", # >= 5
            6:"\|/\n||  / \\", # == 6
        }
        # Selects the correct option from the hashmap
        body = body_parts[self.domain.error_count]
        # And prints it
        self._print_line(body)

        # Prints an empty line
        self._print_line('')
        # Prints the ground
        print("||\n===========")

        # Prints the feedback message
        print(self.domain.msg)
        
        # Returns True if the player has made 6 mistakes
        if self.domain.error_count == 6:
            return True
    
    # Function returns the secret word with hidden characters (•••)
    def _get_secret(self):
        # Clears the screen
        self._clear_screen() 
        # Resets the secret
        self.domain.secret = ""
        # Loops through each letter in the loaded word
        for char in self.domain.word:
            # If the letter is among the guessed letters, show it; otherwise show "•"
            self.domain.secret += char if char in self.domain.hits else "•"
        self._print_interline(f'Word: {self.domain.secret}')

    # Function responsible for printing the input prompt for the user
    def _print_input(self):
        # Prompts for a character
        char = input("\nType a letter:").lower().strip()
        # Clears the feedback message
        self.domain.msg = ""
        # Checks if the player already typed that letter
        if char in self.domain.typed:
            # If yes, adds feedback
            self.domain.msg = "You already tried this letter!"
        else:
            # Otherwise, adds the letter to the typed list
            self.domain.typed += char
            # Checks if the letter is in the word
            if char in self.domain.word:
                # If yes, adds it to hits
                self.domain.hits += char
            else:
                # Otherwise, increments the error counter
                self.domain.error_count += 1
                # And adds an error message for the player
                self.domain.msg = "Wrong guess!"