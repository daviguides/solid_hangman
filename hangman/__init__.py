# versão de um app deve estar no seu pacote principal
__author__ = "Davi Luiz Guides"
__version__ = "0.1.0"

# atalho para a classe principal dessa lib
from .factory import HangmanGameTerminalFactory

# Uma simples facade para a aplicação que aponta para o factory
class HangmanGameApp:
    @classmethod
    def factory(self):
        return HangmanGameTerminalFactory.factory()