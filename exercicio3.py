"""
Preencha uma lista com 20 números inteiros aleatórios sorteados entre 1 e 50 e exiba:
a. a lista com todos os itens armazenados.
b. o somatório de todos os números contidos na lista.
c. o maior número da lista.d.o menor número da lista.
"""

import random

def preenche_lista():
    lista = []
    for i in range(20):
        numero = random.randiant(1,50)
        lista.append(numero)
    return lista

def somar_lista():
    soma = 0
    for item in lista:
        soma += item
    return soma

def maior_numero(lista):
    maior = lista[0]
    for item in lista:
        if item > maior:
            maior = item
    return maior

def menor_numero(lista):
    menor = lista[0]
    for item in lista:
        if item < menor:
            menor = item
    return menor

lista = preenche_lista()
print(lista)
print(f'Somatorio: {somar_lista(lista)}')
print(f'Maior: {maior_numero(lista)}')
print(f'Menor: {menor_numero(lista)}')
