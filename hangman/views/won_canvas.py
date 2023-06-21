from time import sleep
from hangman.common import TerminalCanvas

class WonCanvas(TerminalCanvas):
    """This class defines the screen when the player wins the game,
    with a cool animation :)
    """
    def show(self):
        # Runs the animation 6 times using a loop
        for _ in range(6):
            # Displays frame 1
            self.draw_free_sprite_1()
            # Waits 0.6 seconds
            sleep(.6)
            # Displays frame 2
            self.draw_free_sprite_2()
            # Waits 0.6 seconds
            sleep(.6)
    
    # This function prints frame 1 of the animation
    def draw_free_sprite_1(self):
        # Clears the screen
        self._clear_screen()
        # Prints the secret word
        self._print_interline(f'Word: {self.domain.secret}')
        # Prints the top of the gallows
        print(f"||===:===\n||   :")

        # Prints the middle of the frame
        man = ['','','  O ',' /|\\',' / \\']
        self._print_lines(man)

        # Prints the ground
        print("===========")
        # Prints a success message
        print("You got it right!\n")

    # This function prints frame 2 of the animation
    def draw_free_sprite_2(self):
        # Clears the screen
        self._clear_screen()
        # Prints the secret word
        self._print_interline(f'Word: {self.domain.secret}')
        # Prints the top of the gallows
        print(f"||===:===\n||   :")
        # Prints the middle of the frame
        man = ['    Congratulations!!! ',' \\O/ ','  |',' / \\','']
        self._print_lines(man)

        # Prints the ground
        print("===========")
        # Prints a success message
        print("You got it right!\n")