import os
from abc import ABC

class Canvas(ABC):
    """Classe abstrata que representa um determinado canvas, 
    por exemplo canvas para usar em termina e outro para uma janela no OS
    """
    pass

class TerminalCanvas(ABC):
    """Essa classe abstrata implementa algumas propriedades 
    e funções privadas que seram usadas pelas telas do game
    """
    def __init__(self, domain):
        self.domain = domain
        # constante com o caractere que faz as linhas horizontais ====
        self.LINE_CHAR = "="
        # constante com o caractere que faz as linhas verticais ||
        self.WALL_CHAR = "||"

    @classmethod
    def factory(cls):
        from hangman.domain import domain
        return cls(domain = domain)
    
    def _print_interline(self, value):
        # printa uma linha com espaço uma linha em branco acima e abaixo
        print(f'\n{value} \n')

    def _print_line(self, value):
        # imprime uma linha
        print(f"{self.WALL_CHAR}  {value}")
    
    def _print_lines(self, values):
        # imprime uma sequencia de linhas
        for value in values:
            self._print_line(value)

    # função que limpa a tela
    def _clear_screen(self):
        # verifica que é um sistema unix (linux, mac)
        if(os.name == 'posix'):
            # se sim roda o comando correpondente
            os.system('clear')
        else:
            # caso o contrário roda o comando para windows
            os.system('cls')