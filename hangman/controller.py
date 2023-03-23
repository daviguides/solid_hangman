"""Esse pacote contem o controller do jogo, é o coração da aplicação
responsável por executar os commands para que o jogo aconteça
"""

# importa a classe abstrata que define o contrato do jogo
from .base import HangmanGameBase

class HangmanGame(HangmanGameBase):
    """ Essa classe implementa o padrão controler que conecta 
    domain e view da aplicação
    essa classe em si basicamente desconhece o que tem no domínio 
    e também desconhece o que tem nas views ele só chama suas funções principais
    """

    # esta é a função principal do jogo que dá inicio
    def start(self):
        # chama a tela de seleção de nível
        # mostra o pronpt seletor de níveis
        # e pega o retorno e atribui a level em load_word
        self.prompt_choices.show()

        # carrega uma palavra com base no nível selecionado
        self.load_word.load()

        # inicia o loop principal do game, o while 
        # caso o game loop tenha sido interrompido retornando true
        if self.hang_canvas.show():
            # mostra a tela de sucesso animada com parabens
            self.won_screen.show()
        else:
            # se não mostra a tela do enforcado com a animação do pobre 
            # homem morrendo
            self.hanged_canvas.show()
            