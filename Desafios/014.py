#Escreva um programa que converta uma temperatura digitada em C e converta para F.
temp=float(input('Digite a temperatura em C: '))
conv=(temp*9/5)+32
print('A temperatura em graus é: {} e em F é: {}'.format(temp, conv))
