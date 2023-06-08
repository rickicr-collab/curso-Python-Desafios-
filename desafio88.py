# faca um programa que ajude um jogador da megasena a criar palpites. o programa vai perguntar quantos jogos serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrado tudo em uma lista composta

# ---------- Resolução do Desafio --------------#

from random import randint
from time import sleep
palpites = []
jogos = []
print('-=-' * 15)
print('            Jogo da Megasena            ')
print('-=-' * 15)
quant = int(input('quantos palpites de jogos você deseja sortear? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in palpites:
            palpites.append(numero)
            cont += 1
        if cont == 6:
            break
    palpites.sort()
    jogos.append(palpites[:])
    palpites.clear() 
    tot += 1     
print('-=' * 3, f'Sorteando {quant} jogos', '-=' * 3)
print('Iniciando o sorteio....')
print('-=-' * 15)
sleep(5)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(2)
print('-=-' * 15)
print('Boa sorte !!!')

# ---------- Documentarios sobre o codigo ---------------#
# Importanto blibliotecas 
    # Random → metodo randint = para gerar numeros aleatorio com o paramentro especifo 
    # time → metodo sleep = gerá um tempo de atraso com valor pré definido 

# criando variaveis e lista exigidas 
    # criando lista temporaria palpites para que seja armazenados os dados e depois copiado para lista final jogos
    # criado lista final jogos para que seja armazenados os valores e exibidos no final do programa 
    # criado uma variavel chamada quant → que vai perguntar ao usuario atravez do teclado a quantidade de jogos solicitados para sorteio
    # variavel tot → representando o total de valores a serem processados a partir da quantidade pré definida na variavel quant

# criado um laço while:
    # criada uma condição para que o valor de tot seja menor ou igual ao valor da variavel quant:
        # criada uariavel com valor predefinido cont = 0
            # criado um laço while True:
                # variavel numero criada recebendo a função randint(1, 60) → criando numeros aleatorios nesse intervalo pré definido
                # criando uma condição if para cada valor gerado pelav função randint dentro dda variavel numero que não esteja dentro da lista palpites.
                    # seja adicionado na lista pelpites usando o comando palpites.append(numero)
                    # realizando contador para cada valor inserido dentro da lista 
                # criando uma condição if para que quando o contador atinga um valor de contagem igual a 6:
                    # saia do laço while usando a função break
            # organize a lista temporaria palpites usando a função sort()
            # realize uma copia dos dados de palpites para a lista definitiva jogos usando o comando → jogos.append(palpites[:])
            # realiza a limpeza dos dados da lista temporaria palpites 
            # informando que tot seja contabilizado em + 1 nos valores

# criando um print informando a quantidade de jogos a ser sorteado 
# criando um print simulando um delai de sorteio pelo programa 
# usando a função sleep com parametro (5) para realizar o atraso da simulação em 5 segundos 
# criando um laço for :
    # com o indice e as linhas enumeradas dentro da lista jogos
    # realizando o print formatado mostrando o jogo pelo indice e linha de forma ordenada 
    # usando a função sleep com parametro (2) para que cada jogo leve dois segundo para realizar o sorteio
# criado um print de boa sorte ao usuario 
