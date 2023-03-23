"""Esse pacote contem a classe abastrata do jogo da forca com a assinatura esperada
"""
from abc import ABC
# importa classes abastratas e não classes concretas
# pois o jogo pode ter mais de uma implementação um para terminal 
# outra para web por exemplo
from .common import Canvas, WordLoader

from .domain import HangmanDomain


class HangmanGameBase(ABC):
    """ Essa classe abstrata define a assinatura que se espera de uma 
    implementação do jogo da força contenha
    """
    def __init__(self, 
            # modelo do jogo
            domain: HangmanDomain,
            # o carregador de palavra
            file_loader: WordLoader,
            # a tela de opção de nível
            prompt_choices: Canvas,
            # a tela com a forca
            hang_canvas: Canvas,
            # a tela com o parabens
            won_screen: Canvas,
            # a tela com o enforcado
            hanged_canvas: Canvas):

        #abaixo a assinatura da classe é setada em suas respectivas propriedades
        self.domain: HangmanDomain = domain
        self.prompt_choices: WordLoader = prompt_choices
        self.load_word: Canvas = file_loader
        self.hang_canvas: Canvas = hang_canvas
        self.won_screen: Canvas = won_screen
        self.hanged_canvas: Canvas = hanged_canvas
