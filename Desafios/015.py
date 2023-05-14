# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
#ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e 0,15 por Km rodado.
dias=int(input('Informe a quantidade de dias que o carro ficou alugado: '))
km=float(input('Qual a kilometragem percorrida pelo carro alugado: '))
pago=(dias*60) + (km*0.15)
print('O valor total a pagar é: {:.2f}'.format(pago))

