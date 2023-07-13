'''Faça um programa que tenha uma função
chamada maior(), que receba varios paramentros
com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior'''

from time import sleep

def titulo(msg):
    tam = len(msg) + 2
    print('-' * tam)
    print(msg)
    print('-' * tam)

def maior(* num):
    cont = maior = 0
    for valor in num:
        print(f' {valor}...', end = '', flush = True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f' → Foi digitado ao todo {cont} numeros!')
    print(f'O número encontrado sendo o maior foi {maior}')


# Programa principal 
titulo(f'  {" Analisando Valores "}')
maior(2, 4, 6, 8, 10, 25)
titulo(f'  {" Analisando Valores "}')
maior(4, 6, 8, 9, 3)
titulo(f'  {" Analisando Valores "}')
maior(10, 2, 25, 3)
titulo(f'  {" Analisando Valores "}')
maior(9)
titulo(f'  {" Analisando Valores "}')
maior(0)