#melhore o jogo do Desafio 028 onde o computador vai pensar um numero entre 0 e 10. só que agora o jogador vai tentar adivinhas até acertar mostrando no final quantos palputes foram necessarios para vencer.
from random import randint
import emoji
from time import sleep

computador = randint(0, 10)
print('''=== Bem vindo ao jogo da adivinhação ===''')
print('''o jogo consiste em adivinhas qual numero 
eu pensei no momento vamos comecar?''')
print('Estou Pensando........')
sleep(5)
print('''HUMM... acabei de pensar diga qual é''')
acertou = False # varivavel acertou declarada incialmente como false
palpites = 0 #varavel palpites funcionando como contador 
while not acertou: # condição while quando nega a variavel acertou
    jogador = int(input('Qual o seu palpite? ')) # variavel jogador criada para informar o valor 
    palpites += 1 # variavel palpites com acrescimenos de valores como contagem
    if jogador == computador: # condição if dentro do while quando jogador e computador possui valores iguais 
        acertou = True # então a condição va variavel acertou e mudada para True
    else: # condição else criada para informar que os valores foram diferentes e informando mais informacoes auxiliando para que a condição do if seja alcançada e o programa finalizado 
        if jogador < computador:
            print('Mais!!\u2B06\uFE0F   Tente novamente.')
        elif jogador > computador:
            print('Menos!!\u2B07\uFE0F  Tente novamente.')
print(' \U0001f389 Acertou!!\U0001f389 com {} palpites'.format(palpites))