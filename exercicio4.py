"""
Solicite os nomes e as idades de 10 pessoas. 
Armazene os nomes em uma lista e as idades em outra lista
.Na sequência, exiba os nomes de todas as pessoas que possuemidade maior ou igual a 18 anos.
"""

nomes = []
idades = []

cont = 0
while cont < 10:
    try:
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        nomes.append(nome)
        idades.append(idade)
        cont += 1
    except ValueError:
        print('ERRO: A idade deve ser um valor inteiro')

print(nomes)
print(idades)

for indice in range(len(idades)):
    if idades[indice] >= 18:
        print(f"{nomes[indice]} - {idades[indice]}")