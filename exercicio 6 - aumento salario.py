# Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.
# Lembre-se que o aumento está em porcentagem.

salario = float(input('Digite o seu salário: R$ '))
aumento_perc = float(input('Digite o percentual de aumento: '))

aumento = (aumento_perc / 100) * salario
novo_sal = aumento + salario

print(f'O aumento foi de R$ {aumento:.2f} ')
print(f'O novo salário é de R$ {novo_sal:.2f} ')
