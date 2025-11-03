
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir_no_inicio(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.inicio
        self.inicio = novo_no


    def inserir_no_fim(self, valor):
        novo_no = No(valor)
        if self.inicio is None:
            self.inicio = novo_no
            return
        atual = self.inicio
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no
        return
    
    def tamanho(self):
        if self.inicio is None:
            return 0
        atual = self.inicio
        total = 0
        while atual:
            total += 1
            atual = atual.proximo
        return total


    def exibir(self):
        atual = self.inicio
        if atual is None:
            print('Lista vazia')
            return
        while atual:
            print(atual.valor, end='')
            if atual.proximo:
                print(' -> ', end='')
            atual = atual.proximo
        print()
    

    def remover_inicio(self):
        if self.inicio is None:
            print('Lista vazia')
            return
        self.inicio = self.inicio.proximo

    def remover_fim(self):
        if self.inicio is None:
            print('Lista vazia')
            return
        if self.inicio.proximo is None:
            self.inicio = None
            return
        atual = self.inicio
        while atual.proximo.proximo:
            atual = atual.proximo
        atual.proximo = None

if __name__ == "__main__":
    lista = ListaEncadeada()
    lista.inserir_no_fim(10)
    lista.inserir_no_fim(20)
    lista.inserir_no_fim(30)
    print("Lista após inserções no fim:")
    lista.exibir()  # Deve mostrar: 10 -> 20 -> 30

    lista.inserir_no_inicio(5)
    print("Lista após inserção no início:")
    lista.exibir()  # Deve mostrar: 5 -> 10 -> 20 -> 30

    lista.remover_inicio()
    print("Lista após remover o início:")
    lista.exibir()  # Deve mostrar: 10 -> 20 -> 30
    lista.remover_fim()
    print("Lista após remover o fim:")
    lista.exibir()

    print("Tamanho da lista:", lista.tamanho())  # Deve mostrar: 2