''' O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual
de lucro do distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa que
receba o preço de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual
de impostos. Calcule e mostre:
 a) O valor correspondente ao lucro do distribuidor;  
 b) O valor correspondente aos impostos;
 c) O preço final do veículo.
 '''

precoFabrica = float(input('Digite o valor do carro: '))
percLucro = float(input('Digite o percentual do lucro: '))
percImposto = float(input('Digite o percentual de imposto: '))

lucro = precoFabrica * (percLucro / 100) 
imposto = precoFabrica * (percImposto/100)

valorFinal = precoFabrica + lucro + imposto 
print(f'O lucro do distribuidor foi de R${lucro} corresponde ao imposto {imposto} e R${valorFinal} é o valor finao do veiculo')
