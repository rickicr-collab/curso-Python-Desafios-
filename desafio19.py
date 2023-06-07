#-------------Desafio 19-------------------------#
#Um professor quer sortear um dos seus quatros alunos para apagar o quadro.faca um programa que ajude ele,lendo o nome deles e escrevendo o nome do escolhido.
#opção 01
import random
a1 = input('digite o primeiro aluno:')
a2 = input('digite o segundo aluno:')
a3 = input('digite o terceiro aluno:')
a4 = input('digite o nome do quarto aluno:')
lista = [a1,a2,a3,a4]
escolhido = random.choice(lista)
print('Parabens:{} !, você foi o escolhido'.format(escolhido))
#opção 02
from random import choice
alunos = ('Vera, Antonio, Viviane, Marcos');
lista = ['Vera','Antonio','Viviane','Marcos']
escolhido = choice(lista)
print('A ordem dos alunos foi {}, e o escolhido foi {}'.format(alunos, escolhido))
#---------------------------------------------------------
