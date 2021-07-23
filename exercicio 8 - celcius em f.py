# Faça um programa que peça a temperatura em graus fº, transforme em graus celcius
# F = 9/5 * C + 32.

F = float(input('Digite um valor de temperatura: '))

C = (F - 32) / 1.8

print(f"{F:.1f}º F corresponde a {C:.1F}ºC")
