"""
Solicite 10 números inteiros ao usuário e armazene os números pares em uma lista,
e os números ímpares em outra lista.
Exiba as duas listas ao usuário.
"""

pares = []
impares = []

cont = 0

while cont < 10:  
    try: #preenche uma lista com 10 números
     numero = int(input("Número: "))

     if numero % 2 == 0:
        pares.append(numero)

     else:
        impares.append(numero)
        cont += 1
    except ValueError:
        print ("ERRO. O número digitado deve ser inteiro")
print(pares)
print(impares)