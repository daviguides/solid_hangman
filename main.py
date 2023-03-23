"""este módulo main somente carrega o app
"""
from hangman import HangmanGameApp


if __name__ == "__main__":
    # Chama o factory do app
    hg = HangmanGameApp.factory()
    # define se vai estar com debug ligado
    hg.domain.debug = True
    # ínicia o jogo
    hg.start()
