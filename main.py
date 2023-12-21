import random

numeros = list(range(1, 30))
print(numeros)

random.shuffle(numeros)

for numero in numeros:
    print(numero)
