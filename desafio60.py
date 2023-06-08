#faca um programa que leia um numero qualquer e mostre o seu fatorial
#ex - 5! = 5x4x3x2x1 =120
# usando bliblioteca math
# 01 primeira forma 
from math import factorial # importando a bliblioteca math
n = int(input('Digite um valor :')) # gerar uma variavel para ser informado no teclado 
f = factorial(n) # criada a variavel f realizando o fatorial do valor inserido na variavel n
print(f) # print variavel f
#----------------------------------------------------------------------------
#02 segunda forma
print('-=-' * 15)
print(' Simulador de Fatorial')
print('-=-' * 15)
num = int(input('Digite um numero para saber seu fatorial:'))
resultado = 1 # criado variavel resultado atribuido o valor 1 inicial
count = num # criado a variavel count recebendo o valor em num
print('Calculando {}!'.format(num), end='') # informaçoes sobre o fatorial do valor inserido
while count > 0: # condição while com contador sendo maior que 0
    print(' {} '.format(count), end='') # imprimindo as informaçoes referente ao contador
    print(' x ' if count > 1 else ' = ', end='') # imprimindo as iinformaaçoes mais detalhada sobre as operaçoes realizada no fatorial inserindo condições para caracteres na impressão das informações
    resultado *= count # variavel resultado realizando multiplicação a partir dos valores de count lembrando que count recebeu os valores da variavel num
    count -= 1 # variavel count realizando a operação onde o valor recebido de count será subtraido para seus valores menores até a chegada de zero
print('{}'.format(resultado), end="") # imprimindo informaçoes detalhadas sobre o resultado da operação
