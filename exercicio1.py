"""
Solicite 10 números inteiros ao usuário e armazene os números pares em uma lista,
e os números ímpares em outra lista.
Exiba as duas listas ao usuário.
"""

pares = []
impares = []

for n in range(10):
    num = int(input('Insira um número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(pares)
print(impares)
