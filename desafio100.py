'''Faça um programa que tenha uma lista
chamada números e duas funções chaamadas 
sorteio() e somapar().A primeira função vai sortear
5 números e vai coloca-los dentro da lista e a segunda funçao
vai mostrar a soma enre todos os valores PARES sorteados 
pela função anterior '''

from random import randint
from time import sleep

def titulo(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f' {msg}')
    print('-' * tam)
    
def titulo2(msg):
    tam = len(msg) + 3
    print('-' * tam) 
    print(f' {msg}')
    print('-' * tam)
    
      
def sorteia(lista):
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print('Sorteando...', end = '')
        print(f'{n} ', end = '', flush = True)
        sleep(0.6)
  
  
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor  % 2 == 0:
            soma += valor
        print('Somando valores....', end = '', flush = True)
        sleep(0.7)
    print(f'\nA soma dos valores pares da {lista} são {soma}')
            


titulo(f' {" Sorteio de numeros "}')     
numeros = list()
sorteia(numeros)
print('\nO numeros sorteados foram → ', numeros)
titulo2(f' {" Soma dos Numeros Pares "}')
somapar(numeros)
