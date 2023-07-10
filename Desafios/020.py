'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

import random
aluno=str(input('Informe o primero aluno: '))
aluno1=str(input('Informe o segundo aluno: '))
aluno2=str(input('Informe o terceiro aluno: '))
aluno3=str(input('Informe o quarto aluno: '))
lista=[aluno, aluno1, aluno2, aluno3]
print('O aluno sorteado foi: ',random.sample(lista, len (lista)))