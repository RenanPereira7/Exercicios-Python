# Faça um Programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão 
# ser compostos pelos elementos intercalados dos dois outros vetores.


Vet1 = []
Vet2 = []
Vet3 = []
qtd = 5

for i in range (qtd):
    Vet1.append(int(input('Digite o {}o. elemento do Vetor1: ' .format(i+1))))

for i in range (qtd):
    Vet2.append(int(input('Digite o {}o. elemento do Vetor2: ' .format(i+1))))

print('Vetor1: {}'.format(Vet1))
print('Vetor2: {}'.format(Vet2))

# Vet1 = [1, 4, 6]
# Vet2 = [2, 4, 3]
# Vet3 = [1, 2, 4, 4, 6, 3]

for i in range(qtd):
    Vet3.append(Vet1[i])
    Vet3.append(Vet2[i])

print('Vetor3: {}' .format(Vet3))

'''
###########
# Utilizando Vetores

qtd = 5
V1 = [0]*qtd
V2 = [0]*qtd
V3 = [0]*(qtd*2)


for i in range (qtd):
    V1[i] = int(input('Digite o {}o. elemento do Vetor1: ' .format(i+1)))

for i in range (qtd):
    V2[i] = int(input('Digite o {}o. elemento do Vetor2: ' .format(i+1)))

print('Vetor1: {}'.format(V1))
print('Vetor2: {}'.format(V2))

# Vet1 = [1, 4, 6]
# Vet2 = [2, 4, 3]
# Vet3 = [1, 2, 4, 4, 6, 3]

for i in range(qtd):
    V3[i*2] = V1[i]
    V3[i+1] = V2[i]

print('Vetor3: {}' .format(V3))

'''