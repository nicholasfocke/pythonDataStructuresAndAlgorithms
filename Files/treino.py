def fibonacci(a, b):
    maior = max(a, b)

    anterior = 0
    atual = 1

    print(anterior)

    while atual <= maior:
        print(atual)
        proximo = atual + anterior
        anterior = atual
        atual = proximo

fibonacci(3, 10)
        