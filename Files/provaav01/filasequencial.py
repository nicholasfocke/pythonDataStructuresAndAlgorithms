class FilaSequencial:
    def __init__(self, capacidade = 5):
        self.capacidade = capacidade
        self.dados = [None] * self.capacidade
        self.inicio = 0
        self.fim = 0
        self.tamanho = 0

    def esta_vazia(self):
        return self.tamanho == 0
    
    def esta_cheia(self):
        return self.tamanho == self.capacidade
        
    def enqueue(self, valor):
        if self.esta_cheia():
            print("Fila cheia! não é possivel inserir.")
            return
        self.dados[self.fim] = valor
        self.fim = (self.fim + 1) % self.capacidade
        self.tamanho += 1

    def dequeue(self):
        if self.esta_vazia():
            print("Fila vazia!!!")
            return
        valor = self.dados[self.inicio]
        self.dados[self.inicio] = None

        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        return valor
    
    def expand(self):
        nova_capacidade = self.capacidade * 2
        novo_dados = [None] * nova_capacidade

        for i in range(self.tamanho):
            novo_dados[i] = self.dados[(self.inicio + i) % self.capacidade]
        self.capacidade = nova_capacidade
        self.dados = novo_dados
        self.inicio = 0
        self.fim = self.tamanho
        print(f'Fila expandida para {self.capacidade} posições.')
    
    def exibir(self):
        if self.esta_vazia():
            print("Fila vazia!!!")
            return 
        print("Fila:", end='')
        for i in range(self.tamanho):
            print(self.dados[(self.inicio + i) % self.capacidade], end=' ')
        print()
    
if __name__ == '__main__':
    fila = FilaSequencial()
    fila.exibir()
    for i in range(1, 6):
        fila.enqueue(i)
        fila.exibir()
    fila.enqueue(6)
    fila.dequeue()
    fila.exibir()
    fila.enqueue(6)
    fila.exibir()
    fila.dequeue()
    fila.exibir()
    fila.expand()
    fila.exibir()
    fila.enqueue(7)
    fila.exibir()
    fila.enqueue(8)
    fila.exibir()
