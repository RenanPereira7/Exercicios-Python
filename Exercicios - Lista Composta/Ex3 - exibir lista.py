# Faça um programa que receba dois inteiros x e y e, em seguida, 
# exiba uma lista com todos os valores entre x e y (funcionando 
# tanto para x ≤ y como para x ≥ y. 
# Exemplos:
# x = 2; y = 6 -> Resultado = [2, 3, 4, 5, 6]
# x = 10; y = 7 -> Resultado = [10, 9, 8, 7]

x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))

Resultado = []

if (x <= y):
    for i in range(x, y + 1):
        Resultado.append(i)
else:
    for i in range(x, y - 1, -1):
        Resultado.append(i)

print(Resultado)

