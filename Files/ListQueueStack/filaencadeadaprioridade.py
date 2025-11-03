class No:
    def __init__(self, valor, prioridade):
        self.valor = valor
        self.prioridade = prioridade  
        self.proximo = None

class FilaPrioridade:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.tamanho == 0

    def enqueue(self, valor, prioridade):
        novo_no = No(valor, prioridade)
        if self.esta_vazia() or prioridade > self.inicio.prioridade:
            novo_no.proximo = self.inicio
            self.inicio = novo_no
        else:
            atual = self.inicio
            while (atual.proximo is not None and atual.proximo.prioridade >= prioridade):
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1

    def dequeue(self):
        if self.esta_vazia():
            print("Fila vazia")
            return
        valor_remover = self.inicio.valor
        self.inicio = self.inicio.proximo
        self.tamanho -= 1
        return valor_remover

    def count(self):
        return self.tamanho

    def display(self):
        atual = self.inicio
        if atual is None:
            print("Fila vazia")
            return
        while atual:
            print(f"({atual.valor}, prioridade={atual.prioridade})", end='')
            if atual.proximo:
                print(" --> ", end='')
            atual = atual.proximo
        print()

if __name__ == '__main__':
    fila = FilaPrioridade()
    fila.enqueue('A', 5)
    fila.enqueue('B', 8)
    fila.enqueue('C', 3)
    fila.enqueue('D', 8)
    fila.enqueue('E', 10)
    fila.display() 
    print('Total de elementos:', fila.count())
    fila.dequeue()
    fila.display()
    print('Total de elementos:', fila.count())
    fila.dequeue()
    fila.display()
    print('Total de elementos:', fila.count())
