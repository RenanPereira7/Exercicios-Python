# Faça um Programa que leia 10 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

vet = []
vetPar = []
vetImpar = list()
qtd = 3

'''
for i in range(qtd): # range(inicio, fim, passo)
    vet.append(int(input('Digite o {}o. valor: ' .format(i+1))))

    if(vet[i] % 2 == 0):
        vetPar.append(num)
    else:
        vetImpar.append(num)

'''
for i in range(qtd): # range(inicio, fim, passo)
    num = int(input('Digite o {}o. valor: ' .format(i+1)))
    vet.append(num)

    if (num % 2 == 0):
        vetPar.append(num)
    else:
        vetImpar.append(num)

# vetPar.sort() # sort = método de ordenação
print(vet)
print(sorted(vetPar))
print(vetImpar)



    

