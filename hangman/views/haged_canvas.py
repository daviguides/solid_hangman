from time import sleep
from hangman.common import TerminalCanvas

class HangedCanvas(TerminalCanvas):
    """Essa classe define a tela quando a pessoa perde o jogo
    com uma animação legal :)
    """
    def show(self):
        # define mensagem
        self.domain.msg = 'Enforcado!!!'
        # roda 3 vezes a animação usando um for
        for i in range(3):
            # chama o quadro 1
            self.draw_free_sprite_1()
            # aguarda 0,6 segundos
            sleep(.6)
            # chama o quadro 2
            self.draw_free_sprite_2()
            # aguarda 0,4 segundos
            sleep(.4)
        # chama o quadro 3
        self.draw_free_sprite_3()
        # aguarda 0,5 segundos
        sleep(.5)

    
    def draw_free_sprite_1(self):
        # limpa a tela
        self._clear_screen()
        # imprime a palavra
        self._print_interline(f'Palavra: {self.domain.word}')
        # imprime o topo da forca
        print(f"||===:===\n||   :")
        # imprime o meio do quadro
        man = [f'\O/    {self.domain.msg} ',' |','/ \\','']
        self._print_lines(man)
        # imprime o chão
        print("||\n===========")
    
    def draw_free_sprite_2(self):
        # limpa a tela
        self._clear_screen()
        # imprime a palavra
        self._print_interline(f'Palavra: {self.domain.word}')
        # imprime o topo da forca
        print(f"||===:===\n||   :")
        # imprime o meio do quadro
        man = [f'/O\     ',' |','/ \\','']
        self._print_lines(man)
        # imprime o chão
        print("||\n===========")

    def draw_free_sprite_3(self):
        # limpa a tela
        self._clear_screen()
        # imprime a palavra
        self._print_interline(f'Palavra: {self.domain.word}')
        # imprime o topo da forca
        print(f"||===:===\n||   :")
        # imprime o meio do quadro
        man = [f' O     {self.domain.msg} ','/|\\','/ \\','']
        self._print_lines(man)
        # imprime o chão
        print("||\n===========\n")
