#Faça um programa que receba 4 notas de um aluno, calcule e imprima a média aritmética das notas.

N1 = float(input('Digite a nota 1: '))
N2 = float(input('Digite a nota 2: '))
N3 = float(input('Digite a nota 3: ')) # Decimais - float
N4 = input('Digite a nota 4: ') # ao nao declarar a variavel vem como padrão sting

N4 = float(N4)
media = (N1 + N2 + N3 + N4) / 4
 
print(f'A média foi: {media:.2f} ')