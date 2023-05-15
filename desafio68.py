# Faça um programa que jogue par ou impar com o computador.
# o jogo será interrompido quando o jogador perder.
# mostre o total de vitorias consecutivas que ele conquistou no final do jogo.
from random import randint
vitoria = 0
while True:
    jogador = int(input('Digite o valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    print(f'O jogador jogou {jogador} e o computador jogou {computador}. total de {total}' , end = ' ')
    if total % 2 == 0:
        print('Deu PAR!')
    else:
        print('Deu IMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Jogador Venceu PARABENS!!!') 
            vitoria += 1
        else:
            print('jogador Você perdeu!!!')
            break 
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu PARABENS!!!')
            vitoria += 1
        else:
            print('Você perdeu!!!')
            break 
    print('Vamos jogar novamente...')
print(f'FIM DE JOGO!!! você Venceu a partida {vitoria} vezes')
       
        
        