#Faça um script que leia dois números e mostre o resto da divisão de um número pelo outro.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

potencia = num1 ** num2
print(f'{num1} elevado a {num2} é: {potencia} ')

resto = num1 % num2
print(f'O {num1} foi dividido por {num2} tem como resto: {resto} ')

divisao1 = num1 // num2
print(f'O {num1} dividido por {num2} tem como resultado: {divisao1} ')

divisao = num1 / num2
print(f'O {num1} dividido por {num2} é: {divisao:.2f} ')

