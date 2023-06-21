from time import sleep
from hangman.common import TerminalCanvas

class HangedCanvas(TerminalCanvas):
    """This class defines the screen when the player loses the game,
    with a cool animation :)
    """
    def show(self):
        # Sets the message
        self.domain.msg = 'Hanged!!!'
        # Runs the animation 3 times using a loop
        for i in range(3):
            # Displays frame 1
            self.draw_free_sprite_1()
            # Waits 0.6 seconds
            sleep(.6)
            # Displays frame 2
            self.draw_free_sprite_2()
            # Waits 0.4 seconds
            sleep(.4)
        # Displays frame 3
        self.draw_free_sprite_3()
        # Waits 0.5 seconds
        sleep(.5)

    def draw_free_sprite_1(self):
        # Clears the screen
        self._clear_screen()
        # Prints the word
        self._print_interline(f'Word: {self.domain.word}')
        # Prints the top of the gallows
        print(f"||===:===\n||   :")
        # Prints the middle frame
        man = [f'\O/    {self.domain.msg} ',' |','/ \\','']
        self._print_lines(man)
        # Prints the ground
        print("||\n===========")
    
    def draw_free_sprite_2(self):
        # Clears the screen
        self._clear_screen()
        # Prints the word
        self._print_interline(f'Word: {self.domain.word}')
        # Prints the top of the gallows
        print(f"||===:===\n||   :")
        # Prints the middle frame
        man = [f'/O\\     ',' |','/ \\','']
        self._print_lines(man)
        # Prints the ground
        print("||\n===========")

    def draw_free_sprite_3(self):
        # Clears the screen
        self._clear_screen()
        # Prints the word
        self._print_interline(f'Word: {self.domain.word}')
        # Prints the top of the gallows
        print(f"||===:===\n||   :")
        # Prints the middle frame
        man = [f' O     {self.domain.msg} ','/|\\','/ \\','']
        self._print_lines(man)
        # Prints the ground
        print("||\n===========\n")
