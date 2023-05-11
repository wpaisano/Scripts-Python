# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n=input('Informa um número para saber as informações sobre ele: ')
print('O número que você digitou foi: ',type(n))
print('É um número: ? ', n.isalpha())
print('É alfabético ? ', n.isalnum())