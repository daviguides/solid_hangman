from hangman.common import TerminalCanvas

class PromptChoicesCanvas(TerminalCanvas):
    def __init__(self,
            domain = None,
            question='Escolha um nível', 
            options=[]):

        self.LINE_CHAR = "="
        self.WALL_CHAR = "||"

        self.domain = domain
        self.question = question
        self.options = options or ['Fácil', 'Difícil']

    @classmethod
    def factory(cls, 
            question='Escolha um nível', 
            options=[]):
        from .  .domain import domain
        return cls(domain = domain,
                    question = question,
                    options = [])
    

    def show(self):
        self.question_lenght = len(self.question)+2
        
        self._clear_screen()
        self.print_separator()
        self.print_title()

        value = 0
        for option in self.options:
            value =  value + 1
            self.print_option(value, option)
        
        self.print_separator()
        
        self.domain.level = self.print_input()

    def print_separator(self): 
        print(self.LINE_CHAR*(self.question_lenght+4))

    def print_title(self):
        print(f'{self.WALL_CHAR} {self.question} {self.WALL_CHAR}')
    
    def print_option(self, value, caption):
        option = f' [{value}] - {caption}'
        spaces = (self.question_lenght - len(option)) * ' '
        print(f'{self.WALL_CHAR}{option}{spaces}{self.WALL_CHAR}')

    def print_input(self):
        return int(input("\nDigite o número: ").lower().strip())