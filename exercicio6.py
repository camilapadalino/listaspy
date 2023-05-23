"""
Solicite uma quantidade indeterminada denotasde alunos 
(até que seja informada uma nota menor que zero). 
Após a entrada de dados, exiba:
a. A quantidade de notas que foram informadas.
b.Todas as notas na ordem em que foram informadas.
c.A média aritmética de todas as notas.
d.A quantidade de notas acima da média aritmética calculada.
"""

notas = []


while True:
    try:
        n = float(input('Informe uma nota: '))
        if n < 0:
            break    
        notas.append(n)
    except ValueError:
        print('A nota informadaestá em formato inválido')
print(notas)

print(f'Quantidade de notas: {len(notas)}')

soma = 0
for item in notas:
    soma += item
media = soma / len(notas)
print(f'Média das notas: {media}')


for item in notas:
    if item > media:
        print(item)