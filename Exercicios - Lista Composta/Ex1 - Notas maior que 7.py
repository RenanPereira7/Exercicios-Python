# Faça um programa que leia 10 notas, mostre as notas, a média na tela e 
# quantas notas possui valor maior ou igual a 7.0.
# Verificar se a nota digitada está entre 0 e 10. Caso não esteja, 
# solicitar que o usuário digite novamente

from statistics import mean  

qtd = 5
notas = list() # notas = [] ou 
# notas2 = [0] * qtd

flag = 0

for i in range(0, qtd):
    flag = 0

    '''while True:
        nota = float(input('Digite a nota do {}o. aluno: ' .format(i+1)))
        if (nota >= 0) and (nota <= 10): # if (0 <= nota <= 10):
            break
        '''
    while (flag == 0):
        nota = float(input('Digite a nota do {}o. aluno: ' .format(i+1)))
        if (0 <= nota <= 10):
            flag = 1
        
    notas.append(nota)

soma = 0
for i in range(qtd):
    soma += notas[i]
media = soma / qtd

soma2 = sum(notas)
media2 = soma2 / qtd

media3 = mean(notas)

print(notas)
print('A média foi de: {:.2f}'.format(media))
print('A média foi de: {:.2f}'.format(media2))
print('A média foi de: {:.2f}'.format(media3))


