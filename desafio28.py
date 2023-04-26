#escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobri qual foi o numero escolhido pelo computador.
#o programa deve mostrar na tela se o usuario venceu ou perdeu.
from random import randint
from time import sleep
computador = randint(0, 5) #função que faz o computador "pensar" nume numero aleatório
print('-=-'*20)#caracteres que funcionam com vinheta 
print('Vou pensar num numero entre 0 e 5. tente adivinhar ....')
print('-=-'*20)
jogador  = int(input('Em que numero eu pensei? '))# o jogador tenta adivinhar 
print('PROCESSANDO....')
sleep(3)
if jogador == computador:
    print('PARABENS você me venceu')# print quando o jogador consegue adivinhar o numero aleatorio gérado pelo computador 
else:
    print('GANHEI! Eu pensei no numero {} e não no numero {}.'.format(computador, jogador))#print gerado na tela quando o programa gerá um numero que o jogador não adivinhou usando o formatação das variaveis em suas respectivas ordens 