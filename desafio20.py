#-------------Desafio 20-------------------------#
#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada 
import random #importando a bliblioteca random
n1 = input('digite o primeiro nome:')
n2 = input('digite o segundo nome:')
n3 = input('digite o terceiro nome:')
n4 = input('digite o quarto nome:')
lista = [n1, n2, n3, n4] # criando uma lista com 4 variaveis usando a propriedade input
random.shuffle(lista) #usando a função random.shuffle(lista) para atribuir uma função aleatoria de escolha entre as 4 variaveis criadas anteriormente 
print('Os nomes em ordem de apresentação são: {}'.format(lista))
#-------------------------------------------------------------------