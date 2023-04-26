#-------------Desafio 18-------------------------#
#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno, e tangente desse angulo.
import math #importanto bliblioteca math
ang = float(input('Digite o angulo que deseja saber o seno / cosseno / tangente: '))#variavel ang atribuida com classe primitiva float 
ang1 = math.radians(ang)#variavel criada atribuindo classe math.radians sobre a variavel ang
seno = math.sin(ang1)#variavel criada atribuindo class math.sin sobre a variavel ang
cose = math.cos(ang1)#variavel criada atribuindo classe math.cos sobre a variavel ang
tang = math.tan(ang1)#variavel criada atribuindo classe math.tan sobre a variavel ang
print('>'*50)
print('Com o angulo {}°,\nO seno é {:.2f},\nO cosseno é{:.2f}\nE a tangente é{:.2f}'.format(ang, seno, cose, tang))#print para informar valores propostos nas variaveis 
print('>'*50)
#----------------------------------------------------------------
