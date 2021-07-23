# Crie um script que leia o nome de uma pessoa, bem como, o dia, o mês e o ano de nascimento dela e mostre uma mensagem com a data formatada.
# Ex:‘Ana nasceu no dia 01 de janeiro de 2000’.

nome = input('Digite seu nome: ')
dia = int(input('Digite o dia do seu nascimento: '))
mes = input('Digite o mês do seu nascimento: ')
ano = int(input('Digite o ano do seu nascimento: '))

print(f'{nome} nasceu no dia {dia} de {mes} de {ano}')