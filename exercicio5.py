"""
Faça uma função que recebe como parâmetrouma lista e um número. 
A função deve retornar a quantidade de vezes que o número aparece na lista. 
No programa principal, preencha a lista com 10 números aleatórios e solicite um número ao usuário.
Envie as informaçõespara a função e exiba o seu retorno.
"""

def buscar(lista,numero):
    cont = 0
    for item in lista:
        if item == numero:
            cont += 1
    return cont

lista = []
while len(lista) < 10:
    try:
        numero = int(input('Numero: '))
        lista.append(numero)
    except ValueError:
        print('Erro: O numero digitado deve ser inteiro')
print(lista)

numero = int(input('Informe um numero para buscar na lista: '))
print(f'Quantidade de vezes que {numero} aparece na lista é: {buscar[lista,numero]}')