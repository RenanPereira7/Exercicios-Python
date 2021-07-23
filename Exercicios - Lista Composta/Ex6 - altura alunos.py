# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine 
# quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

from random import randint # importa apenas o randint
from random import random # importa apenas o random
# import random # importa toda a biblioteca randômica

idade = []
altura = list()
qtd = 10
cont = 0

for inc in range(qtd):
    #idade.append(random.randint(5, 40)) # importa toda a biblioteca randômica
    idade.append(randint(5, 40)) # importa apenas o randint

    #altura.append(randint(120, 190))
    #altura.append(round(1 + random.random(), 2)) # importa toda a biblioteca randômica
    altura.append(round(1 + random(), 2)) # importa apenas o random

    # random.random() - gera números randômicos de zero a 1
    # 1 + random.random() - soma 1 ao número randômico
    # round(num, 2) - arredonda para 2 casas decimais

media = sum(altura) / qtd # len(altura)

for i in range(qtd):
    if ((idade[i] > 13) and (altura[i] < media)):
        cont += 1

print('Idade {}' .format(idade))
print('Altura {}' .format(altura))
print(f'{cont} aluno(s) com mais de 13 anos e possuem altura menor que a {media:.2f}')




