from time import sleep
from hangman.common import TerminalCanvas

class WonCanvas(TerminalCanvas):
    """Essa classe define a tela quando a pessoa vence o jogo
    com uma animação legal :)
    """
    def show(self):
        # roda 6 vezes a animação usando um for
        for _ in range(6):
            # chama o quadro 1
            self.draw_free_sprite_1()
            # aguarda 0,6 segundos
            sleep(.6)
            # chama o quadro 2
            self.draw_free_sprite_2()
            # aguarda 0,6 segundos
            sleep(.6)
    
    # Essa função imprime o quadro 1 da animação
    def draw_free_sprite_1(self):
        # limpa a tela
        self._clear_screen() 
        # imprime a palavra
        self._print_interline(f'Palavra: {self.domain.secret}')
        # imprime o topo da forca
        print(f"||===:===\n||   :")

        # imprime o meio do quadro
        man = ['','','  O ',' /|\\',' / \\']
        self._print_lines(man)

        # imprime o chão
        print("===========")
        # imprime mensagem de acerto
        print("Você acertou!\n")

    # Essa função imprime o quadro 2 da animação
    def draw_free_sprite_2(self):
        # limpa a tela
        self._clear_screen()
        # imprime a palavra
        self._print_interline(f'Palavra: {self.domain.secret}')
        # imprime o topo da forca
        print(f"||===:===\n||   :")
        # imprime o meio do quadro
        man = ['    Parabens!!! ',' \O/ ','  |',' / \\','']
        self._print_lines(man)

        # imprime o chão
        print("===========")
        # imprime mensagem de acerto
        print("Você acertou!\n")