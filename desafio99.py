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
        print(f'{valor}...', end = '', flush = True)
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


# ========= Comentarios sobre o Codigo ========= #

# importado bliblioteca time função sleep
'''Importando bliblioteca time função sleep → from time import sleep'''

# função titulo criada:
''' função titulo criada para estilizar o inicio do codigo criado'''

# função maior:
''' Criado função maior que recebe paramento de varios valores com o termo: (* num)'''
''' criado variaveis sendo : maior , cont → ambos recebendo valor inicial 0'''
    # criado laço for → for valor in num:
''' realizado um print formatado mostrando o valor e alguns paramentro sendo eles :
    → print = print(f' {valor}...)
    paramentros:
    paramentro end que limita o fim de linha para o print sem espacos entre os caracteres → end = ''
    parametro flush que foi adotado devido a uma atuazlição no python para a determinada função sleep
    da bliblioteca time que por padrão recebe FALSE → flush = True
    Função sleep com parametro → sleep(0.5)'''
        # criado laço if → if cont == 0:
''' Se a codição do if acima for verdadeira então a variavel criada maior recebe o valor da variavel valor → maior = valor'''
        # condição else:
            #condição if criada → if valor > maior:
''' Se a condição de if sendo o valor informado for maior que o valor da variavel maior.
  → maior = valor'''
# a variavel cont recebe → cont += 1
''' a variavel cont realiza um contador acrescentado os valores digitados
  → cont = Cont + 1 / cont += 1'''
  
# print criados 
''' realizado um print mostrando todos os valores informados 
  → print(f'foi informados ao todo {cont} numeros') '''
''' ralizado um print mostrando o maior numero encontrado
  → print(f'O maior numeor encontrado sendo o maior foi {maior}')'''
  

# programa Principal 

''' Função titulo com paramentro → (' Analisando Valores ')'''
''' Função Maior com paramentros:
    maior = (2, 4, 6, 8, 10, 25)
    maior = (4, 6, 8, 9, 3)
    maior = (10, 2, 25, 3)
    maior = (9)
    maior = (0)
'''