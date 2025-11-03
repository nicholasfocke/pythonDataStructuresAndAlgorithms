class PilhaSequencial:
    def __init__(self, capacidade = 5):
        self.capacidade = capacidade
        self.dados = [None] * self.capacidade
        self.topo = -1  

    def is_empty(self):
        return self.topo == -1

    def push(self, valor):
        if self.topo + 1 == self.capacidade:
            self.expandir()
        self.topo += 1
        self.dados[self.topo] = valor

    def pop(self):
        if self.is_empty():
            print('Pilha vazia!')
            return None
        valor = self.dados[self.topo]
        self.dados[self.topo] = None
        self.topo -= 1
        return valor

    def peek(self):
        if self.is_empty():
            print('Pilha vazia!')
            return None
        return self.dados[self.topo]

    def expandir(self):
        nova_capacidade = self.capacidade * 2
        novo_dados = [None] * nova_capacidade
        for i in range(self.topo + 1):
            novo_dados[i] = self.dados[i]
        self.dados = novo_dados
        self.capacidade = nova_capacidade
        print(f'Pilha expandida para {self.capacidade} posições.')

    def exibir(self):
        if self.is_empty():
            print('Pilha vazia!')
            return
        print('Pilha (base -> topo):', end=' ')
        for i in range(self.topo + 1):
            print(self.dados[i], end=' ')
        print()

if __name__ == "__main__":
    pilha = PilhaSequencial()
    pilha.push(10)
    pilha.push(20)
    pilha.push(30)
    pilha.push(40)
    pilha.push(50)
    pilha.exibir()
    pilha.pop()
    pilha.exibir()
    pilha.push(60)  
    pilha.exibir()
    pilha.push(70)
    pilha.exibir()
    print('Topo da pilha:', pilha.peek())
