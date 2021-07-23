# Faça um programa que calcule e mostre o resultado das seguintes operações:
# A área de um triângulo (Informar base e altura.)
# O volume de um cubo (Informar valor do lado.)
# A área de um círculo  (Informar o raio.)

# a) Triângulo
base_triangulo = float(input('Informe o valor da base do triângulo: '))
altura_triangulo = float(input('Informe o valor da altura do triângulo: '))

area_triangulo = base_triangulo * altura_triangulo / 2
print(f'A área do triangulo é: {area_triangulo}')

# b) Cubo
lado_cubo = float(input('\n\nInforme o valor do lado do cubo: '))

area_cubo = lado_cubo * lado_cubo
volume_cubo = area_cubo ** 3 # Volume = area * area * area
print(f'O volume do cubo é: {volume_cubo} ')

# c) Círculo
raio_circulo = float(input('\n\nInforme o valor do raio do círculo: '))

# pi = 3.14......
import math
area_circulo = math.pi * raio_circulo ** 2
print(f'A área do círculo é: {area_circulo:.2f}')