# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinra necessária para pintá-la, sabendo que cada
# metro de tinta, pinta uma área de 2m.

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = (largura*altura)
qtdetinta = area/2
print('A parede tem uma área de {} e serão necessários {} para pintar toda a parede.'.format(area, qtdetinta))
