#crie um programa que faça o computador jogar jokenpo com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Sua opções: 
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] -Tesoura''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-' * 11)
if computador == 0: # computador escolheu pedra
    if jogador == 0:
        print('EMPATE')    
    elif jogador == 1:
        print('JOGADOR VENÇE')
    elif jogador == 2:
        print('COMPUTADOR VENÇE')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: # computador escolheu Papel
    if jogador == 0:
        print('COMPUTADOR VENÇE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENÇE')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: # computador escolheu tesoura
    if jogador == 0:
        print('JOGADOR VENÇE')
    elif jogador == 1:
        print('COMPUTADOR VENÇE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA!')