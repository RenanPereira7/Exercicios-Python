# Faça um programa que dadas duas listas de cinco elementos com números inteiros 
# (definidos aleatoriamente), exiba uma lista onde cada elemento é a soma dos 
# elementos de mesma posição nas duas primeiras listas.
# Exemplo:
# Lista1 = [1, 4, 6]
# Lista2 = [2, 4, 3]
# ListaResultante = [3, 8, 9]

from random import randint
L1 = list()
L2 = []
LResult = []
qtd = 5


for i in range(qtd):
    L1.append(randint(0, 50))
    L2.append(randint(0, 50))

'''
# Não permite que sejam adicionados números repetidos na lista
cont = 0
for i in range(qtd):
    while True:
        num = randint(0, 10)
        if num not in L1:
            L1.append(num)
            break
        else: # conta os número repetidos do sorteio
            cont += 1
    
    flag = 0
    while (flag == 0):
        num = randint(0, 10)
        if num not in L2:
            L2.append(num)
            flag = 1

print(cont)
'''

for i in range(0, qtd):
    LResult.append(L1[i] + L2[i])



print(L1)
print(L2)
print(LResult)



