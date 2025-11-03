class No:
	def __init__(self, valor):
		self.valor = valor
		self.proximo = None

class PilhaEncadeada:
	def __init__(self):
		self.topo = None
		self.tamanho = 0

	def is_empty(self):
		return self.tamanho == 0

	def count(self):
		return self.tamanho

	def push(self, valor):
		novo_no = No(valor)
		novo_no.proximo = self.topo
		self.topo = novo_no
		self.tamanho += 1

	def pop(self):
		if self.is_empty():
			print("Pilha vazia! Não é possível remover.")
			return 
		valor = self.topo.valor
		self.topo = self.topo.proximo
		self.tamanho -= 1
		return valor

	def peek(self):
		if self.is_empty():
			print("Pilha vazia! Não há topo.")
			return 
		return self.topo.valor

	def display(self):
		atual = self.topo
		if atual is None:
			print("Pilha vazia!")
			return
		while atual:
			print(f"Valor: {atual.valor}")
			atual = atual.proximo

if __name__ == "__main__":
	pilha = PilhaEncadeada()

	pilha.display()
	pilha.push("A")
	pilha.push("B")
	pilha.push("C")

	print("\nPilha após inserções:")
	pilha.display()

	print("\nTopo da pilha:", pilha.peek())

	print("\nRemovendo o elemento do topo:", pilha.pop())

	print("\nPilha após remoção:")
	pilha.display()

	print(f"\nTotal de elementos na pilha: {pilha.count()}")
