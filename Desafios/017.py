'''Faça um progrma que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.'''  # noqa: E501
from math import sqrt
import math
oposto=float(input('Informe o valor do cat oposto: '))
adj=float(input('Informa o valor do cat adj: '))
print(math.sqrt(oposto**2 + adj**2))