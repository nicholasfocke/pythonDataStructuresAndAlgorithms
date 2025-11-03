class No:
	def __init__(self, valor, prioridade):
		self.valor = valor
		self.prioridade = prioridade
		self.proximo = None

class PilhaEncadeadaMonotonica:
	def __init__(self):
		self.topo = None
		self.tamanho = 0

	def push(self, valor, prioridade):
		if prioridade < 1 or prioridade > 10:
			print(f"Rejeitado: prioridade {prioridade} inválida (deve ser 1-10)")
			return
		if self.topo is None or prioridade >= self.topo.prioridade:
			novo_no = No(valor, prioridade)
			novo_no.proximo = self.topo
			self.topo = novo_no
			self.tamanho += 1
		else:
			print(f"Rejeitado: prioridade {prioridade} < topo={self.topo.prioridade}")

	def pop(self):
		if self.topo is None:
			print("Pilha vazia! Não é possível remover.")
			return None
		valor = self.topo.valor
		prioridade = self.topo.prioridade
		self.topo = self.topo.proximo
		self.tamanho -= 1
		return f"Valor: {valor} | Prioridade: {prioridade}"

	def peek(self):
		if self.topo is None:
			print("Pilha vazia! Não há topo.")
			return None
		return f"Valor: {self.topo.valor} | Prioridade: {self.topo.prioridade}"

	def is_empty(self):
		return self.topo is None

	def count(self):
		return self.tamanho

	def display(self):
		atual = self.topo
		if atual is None:
			print("Pilha vazia!")
			return
		while atual:
			print(f"Valor: {atual.valor} | Prioridade: {atual.prioridade}")
			atual = atual.proximo

if __name__ == "__main__":
	pilha = PilhaEncadeadaMonotonica()

	pilha.push("Lavar Carro", 2)
	pilha.push("Comprar Pão", 5)
	pilha.push("Compra Ovo", 5)
	pilha.push("Pagar conta de energia", 8)
	pilha.push("Varrer a casa", 7)  

	print("\nPilha após inserções:")
	pilha.display()

	print("\nTopo da pilha:", pilha.peek())
	pilha.peek()

	print("\nRemovendo o elemento do topo: ", pilha.pop())

	print("\nPilha após remoção:")
	pilha.display()

	print(f"\nTotal de elementos na pilha: {pilha.count()}")
	print("\nTopo da pilha:", pilha.peek())
	pilha.peek()