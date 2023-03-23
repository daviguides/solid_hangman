from hangman.common import TerminalCanvas

class HangCanvas(TerminalCanvas):
    # função principal
    def show(self):
        while True:
            # mostra a tela principal com a forca
            self.draw()

            # Se a pessoa já chegou ao número de erros ou descobriu a palavra
            # interrompe o game loop
            if self.domain.error_count == 6 \
                or self.domain.secret == self.domain.word:
                break

            # Se não abre o input para inserir mais uma letra
            self._print_input()
        return self.domain.secret == self.domain.word

    # desenha tela
    def draw(self):
        # pega o segredo
        self._get_secret()

        # imprime o topo da forca
        print(f"||===:===\n||   :")
        # imprime o cabeça se tiver um erro ou mais
        head = " O" if self.domain.error_count >= 1 else ""
        self._print_line(head)

        # imprime as partes do corpo de acordo com o nível de erros
        body_parts = {
            0:"\n||",
            1:"\n||",
            2:" | \n||", # == 2
            3:"\| \n||", # == 3
            4:"\|/\n||", # >= 4
            5:"\|/\n||  /", # >= 5
            6:"\|/\n||  / \\", # >= 5
        }
        # seleciona opção correta do hashmap
        body = body_parts[self.domain.error_count]
        # e imprime
        self._print_line(body)

        # imprime uma linha vazia
        self._print_line('')
        # imprime o chão
        print("||\n===========")

        # imprime a mensagem de feedback
        print(self.domain.msg)
        
        # se chegou a 6 erros retorna True
        if self.domain.error_count == 6:
            return True
    
    # função retorna a palavra com •••••••
    def _get_secret(self):
        # limpa tela
        self._clear_screen() 
        # limpa segredo
        self.domain.secret = ""
        # faz um loop por cada letra da palavra carregada
        for char in self.domain.word:
            # se a letre estiver nos acertos retorna ela, se não retorna "•"
            self.domain.secret += char if char in self.domain.hits else "•"
        self._print_interline(f'Palavra: {self.domain.secret}')

    # função responsavel por imprimir o input de entrada de caractere para o usuário
    def _print_input(self):
        # imprime o input
        char = input("\nDigite uma letra:").lower().strip()
        # limpa a mensagem de feedback
        self.domain.msg = ""
        # verifica se a pessoa já digitou aquela letra 
        if char in self.domain.typed:
            # se sim adiciona feedback
            self.domain.msg = "Você já tentou esta letra!"
        else:
            # se não adiciona a letra a digitados 
            self.domain.typed += char
            # verifica se a letra esta na palavra
            if char in self.domain.word:
                # se sim adiciona nos acertos
                self.domain.hits += char
            else:
                # se não incrementa o contador de erros
                self.domain.error_count += 1
                # e adiciona mensagem de erro para o usuário
                self.domain.msg = "Você errou!"