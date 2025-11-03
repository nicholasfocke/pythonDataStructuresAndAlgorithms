class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.tamanho == 0

    def enqueue(self, valor):
        novo_no = No(valor)
        if self.esta_vazia():
            self.inicio = self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no
        self.tamanho+=1

    def dequeue(self):
        if self.esta_vazia():
            print("Fila vazia")
            return
        valor_remover = self.inicio.valor
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None
        self.tamanho-=1

        return valor_remover
    
    def exibir(self):
        atual = self.inicio
        if atual is None:
            print("Fila vazia")
            return
        while atual:
            print(atual.valor, end='')
            if atual.proximo:
                print(" --> ", end='')
            atual = atual.proximo
        print()
    
if __name__ == '__main__':
    fila = Fila()
    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)
    fila.exibir()
    fila.dequeue()
    fila.exibir()
