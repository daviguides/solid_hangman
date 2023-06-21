from hangman.common import TerminalCanvas

class PromptChoicesCanvas(TerminalCanvas):
    def __init__(self,
            domain=None,
            question='Choose a level',
            options=None):

        self.LINE_CHAR = "="
        self.WALL_CHAR = "||"

        self.domain = domain
        self.question = question
        self.options = options or ['Easy', 'Hard']

    @classmethod
    def factory(cls,
            question='Choose a level',
            options=None):
        from ..domain import domain
        return cls(domain=domain,
                   question=question,
                   options=options)

    def show(self):
        self.question_length = len(self.question) + 2

        self._clear_screen()
        self.print_separator()
        self.print_title()

        value = 0
        for option in self.options:
            value += 1
            self.print_option(value, option)

        self.print_separator()

        self.domain.level = self.print_input()

    def print_separator(self):
        print(self.LINE_CHAR * (self.question_length + 4))

    def print_title(self):
        print(f'{self.WALL_CHAR} {self.question} {self.WALL_CHAR}')
    
    def print_option(self, value, caption):
        option = f' [{value}] - {caption}'
        spaces = (self.question_length - len(option)) * ' '
        print(f'{self.WALL_CHAR}{option}{spaces}{self.WALL_CHAR}')

    def print_input(self):
        return int(input("\nType the number: ").lower().strip())