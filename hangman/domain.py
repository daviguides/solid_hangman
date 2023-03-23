"""Neste pacotes estão as denifições do dominio de dados 
que será usado pela mesma, o "modelo" de dados
"""
#importa a classe para definir classes abstratas, é como interfaces no java
#em Python
from dataclasses import dataclass, field

@dataclass
class HangmanDomain():
    """Essa aplicação tem apenas um único domínio que o HangmanDomain
    """
    # Level escolhido para joggar
    level:int = field(default=1)

    # Lista de letras digitadas
    typed:list[str] = field(default_factory=list)
    # Lista de letras acertadas
    hits:list[str] = field(default_factory=list)
    # contador de erros
    error_count:int = field(default=0)

    # A palavra correta
    word:str = field(default_factory=str)
    # Segredo
    secret:str = field(default_factory=str)
    # Mensagem de feadback
    msg:str = field(default_factory=str)
    # Se o modo de depuração está ativado
    debug:bool = field(default=True)

# esta cria um singleton do dominio a partir daqui todas as referencias 
# ao domain seram desta única instância
domain = HangmanDomain()