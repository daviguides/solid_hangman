# importa classe e função necessárias para definir uma classe abstrata
from abc import ABC, abstractmethod
# importa função randint do pacote random
from random import randint

class WordLoader(ABC):
    """ Classe meramente formal para representar abastratamente 
    um carregador de arquivo, por exemplo agora eu tenho uma implementação 
    concreta de um word loader por arquivo, mas poderia ter outra 
    para por banco de dados 
    """
    def __init__(self, domain):
        self.domain = domain

    # @abstractmethod
    def get(self) -> str:
        # as classes que implementam essa abstração devem obrigatóriamente
        # conter esse método, espera se que esse método retorne uma string
        pass

    @classmethod
    def factory(cls):
        from hangman.domain import domain
        return cls(domain = domain)

class FileWordLoader(WordLoader):
    """ Essa classe encapsula a função de abrir os arquivos conforme o nível
    selecionado e carregar uma palavra
    """
    def load(self):
        # Se o debug estiver desligado
        if not self.domain.debug:
            # roda a função padrão que faz o carregamento 
            # correto e seleciona a palavra aleatória
            self.domain.word = self.get().lower()
        else:
            # e para efeitos de test do aplicativo se o modo debug 
            # estiver ligado exibe palavras fixas de acordo com o nível
            if (self.domain.level == 1):
                self.domain.word = 'bola'
            else:
                self.domain.word = 'paralelepipedo'

    # implementa o método abstrato get e retorna uma palavra
    def _get(self) -> str:
        # pega o nome do arquivo a ser aberto
        file_name = self._get_file_name()

        # abre o arquivo
        with open(f'./data/{file_name}.txt') as f:
            # lê o conteudo e divida as linhas numa string
            lines = f.read().splitlines()
        
        # pega um número inteiro aleatório enter 0 e o tamanho de linhas - 1
        #  no arquivo carregado
        index = randint(0,len(lines)-1)

        # retorna uma palavra aleatória com base no inteiro
        return lines[index]

    def _get_file_name(self):
        # retorna o nome do arquivo conforme o level a partir de um hashmap 
        # em que o hash(a chave) é o nível
        return {
            1: 'easy_words', 
            2: 'hard_words'
        }[self.domain.level]

class DBWordLoader(WordLoader):
    """ Numa futura melhoria eu poderia utilizar um loader por banco de dados
    como na classe do Hangman eu apenas faço referencia a classe abstrata,
    não será necessário mudar o código de lá apenas a factory da mesma.
    """
    def get(self):
        pass