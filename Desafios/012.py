# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

prd=float(input('Informe o preço do produto: '))
desc=0.05
novopreco=prd-(prd*desc)
print('O valor do produto com desconto é: {}.'.format(novopreco))
