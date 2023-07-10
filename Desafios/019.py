'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido'''
import random
aluno=str(input('Informe o primero aluno: '))
aluno1=str(input('Informe o segundo aluno: '))
aluno2=str(input('Informe o terceiro aluno: '))
aluno3=str(input('Informe o quarto aluno: '))
lista=[aluno, aluno1, aluno2, aluno3]
print('O aluno sorteado foi: ',random.choice(lista))
#print('O aluno embaralhado foi: ',random.shuffle(lista))
#print('O aluno sorteado no intervalo foi: ',random.randint(aluno, aluno3))
