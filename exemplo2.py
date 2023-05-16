
def busca(lista, item):
    for i in lista:  # percorre os itens da lista
        if i == item:  # verifica se o valor é o que está sendo buscado
            return True  
    return False   # se nao encontrar o valor retorna False

lista = []
while True:
    i = int(input('Informe um número inteiro: '))
    if i == 0:
        break
    lista.append(i)
print(lista)

item = int(input('Informe um número para buscar na lista: '))

if busca(lista, item):
    print('O número está contido na lista')
else:
    print('O número {item} não está contido na lista')