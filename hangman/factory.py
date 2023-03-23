"""Esse pacote contem uma o mais factories, padrão que faz o 
assemble de várias classes para para executar um aplicativo
"""
# Importa o HangmanGame
from .controller import HangmanGame

# Essa classe é um padrão factory que monta o jogo da forca para terminal
class HangmanGameTerminalFactory():
    @classmethod
    def factory(cls):
        # importa as classes concretas para montar o jogo para terminal
        from .views import (PromptChoicesCanvas, HangCanvas, 
                                WonCanvas, HangedCanvas)
        # usa o wordloader apartir de arquivos
        from .common import FileWordLoader

        # carrega o singleton do dominio do jogo
        from .domain import domain

        # retorna o jogo montado
        return HangmanGame(
            # carrega o singleton do domain
            domain=domain,
            # utiliza o wordloader de arquivos textos
            file_loader=FileWordLoader.factory(),

            # carrega a tela de escolha de nível para terminal
            prompt_choices=PromptChoicesCanvas.factory(
                question='Escolha um nível',
                options=['Fácil', 'Difícil']
            ),
            # carrega a tela de forca para terminal
            hang_canvas=HangCanvas.factory(),
            # carrega a vitória para terminal
            won_screen=WonCanvas.factory(),
            # carrega a enforcado para terminal
            hanged_canvas=HangedCanvas.factory()
        )
