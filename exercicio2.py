"""
Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
a.Amédia aritmética dos números armazenadosna lista.
b.O somatório dos números pares armazenados na lista.
"""
def preenche_lista():
    lista = []
    cont = 0
    while cont < 10: # lista com 5 itens
        try:
            numero = int(input('Informe um Número: '))
            lista.append(numero)
            cont += 1
        except ValueError:
            print("ERRO. O valor digitado deve ser inteiro")
    print(lista)

# A média aritmética dos números armazenadosna lista.

def calcula_media(lista):
    soma = 0
    for item in lista:
        soma += item
    media = soma / len(lista)
    return media


# O somatório dos números pares armazenados na lista.

def somar_pares(lista):
    soma = 0
    for item in lista:
        if item % 2 == 0:
            soma += item
        return soma


lista = preenche_lista()
print(lista)
print(f'Média da lista: {calcula_media(lista)}')
print(f'Somatória dos números pares: {somar_pares(lista)}')

