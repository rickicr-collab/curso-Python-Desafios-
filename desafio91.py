# crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatorios.Guarde esses resultados em um dicionario.
# no final colocque esse dicionario em ordem sabendo que o vencedro tirou o maior numero do dado

from random import randint
from time import sleep
from operator import itemgetter
jogos = {"jogador1" : randint(1, 6), "jogador3": randint(1, 6),
         "jogador2" : randint(1, 6), "jogador4": randint(1, 6)}

ranking = list()
print('-=-' * 15)
print(f'{"ValoresSorteados":>26}')
for k, v in jogos.items():
    print(f'O jogador {k} tirou {v} no dado.')
    sleep(1)
print('-=-' * 15)
print(f'{"Ranking":>20}')
print(f'{"Colocação:":<10}')
ranking = sorted(jogos.items(), key = itemgetter(1), reverse = True)
for i , v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('-=-' * 15)
# ----------------- Comentarios --------------------------------#

# importando Blibliotecas 
    # biblioteca random → modulo randint
    # Biblioteca time → modulo sleep
    # biblioteca operator → modulo itemgetter
    
# criado dicionario com 4 chaves jogador usando o modulo randint da biblioteca random
# criado lista chamada ranking

# criado condição for:
    # para cada chave e valor em função nome do dicionario.items():
        # print formatado informando que chave (k) tirou valor (v)
        # usando a função sleep dentro do laço com parametro (1) segundo

# atribuindo lista ranking:
    # função sorted(jogos.items())
    # com chave atribuindo função itemgetter posição 1 → key = itemgetter(1)
    # usando ordem reversa atribuindo valor booleano True → reverse = True

# criando laço for:
    # Para cada indiçe e valor no enumerado ranking → for i, v in enumerate(rankink):
        # print formatado mostrando a posição do primeiro ao ultimo lugar com nome do jogador junto com o numero tirado pelo dado → print(f' {i+1}º {v[0]} com {v[1]}')
        # função sleep com atraso de um segundo como parametro → sleep(1)