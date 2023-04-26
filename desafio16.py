#--------------Desafio 16------------------------#
#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira 
import math
num = float(input('Digite um numero?'))
print('-'*20)
print('O numero {} tem a parte inteira: {}'.format(num, math.floor(num)))
print('-'*20)
#------------------------------------------------------------------
