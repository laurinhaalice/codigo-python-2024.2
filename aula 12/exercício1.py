class Armario:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.gavetas = [["" for _ in range(colunas)] for _ in range(linhas)]

    def atribuir_gaveta(self, linha, coluna, nome_aluno):
        if 0 <= linha < self.linhas and 0 <= coluna < self.colunas:
            self.gavetas[linha][coluna] = nome_aluno
        else:
            print("Posição inválida!")

    def mostrar_armario(self):
        for linha in self.gavetas:
            print(linha)

# Criando um armário 5x5
armario = Armario(5, 5)

# Atribuindo alunos às gavetas
armario.atribuir_gaveta(0, 0, "Alice")
armario.atribuir_gaveta(1, 2, "Bruno")
armario.atribuir_gaveta(3, 4, "Carla")

# Mostrando o estado atual do armário
armario.mostrar_armario()