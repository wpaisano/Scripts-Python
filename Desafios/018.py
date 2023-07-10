'''Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo'''

import math
angulo=float(input('Informe o valor de um angulo para descobrir o seno, cosseno e a tangente do mesmo: '))
angulorad=math.radians(angulo)
print('seno: ',math.sin(angulorad))
print('cosseno: ',math.cos(angulorad))
print('tangente: ',math.tan(angulorad))
