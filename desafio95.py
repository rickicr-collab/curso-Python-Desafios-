# Aprimmore o desafio 93 para que ele funcione com varios jogadores , incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador 


times = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome:')).capitalize().strip()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   para {c+1}ª partida quantos gols?')))
    jogador['gols'] = partidas[:]
    jogador['totals'] = sum(partidas)
    times.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]:')).upper()[0]
        if resp in 'SN':
            break
        print('ERRo! - Digite apenas opções S ou N.')
    if resp == 'N':
        break
    
print('-=-' * 20)
print('cod ', end = '')
for i in jogador.keys():
    print(f'{i:<15}', end = '')
print()
print('-' * 40)
for k, v in enumerate(times):
    print(f'{k:>3} ', end = '')
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()
print('-' * 40)
while True:
    buscar = int(input('Mostrar dados de qual jogador( 999 - para parar): '))
    if buscar == 999:
        break
    if buscar >= len(times):
        print(f'ERRO! - Não existe dados do jogador com {buscar} digitado na busca.')
    else:
        print(f'Levantamento do jogador {times[buscar]["nome"]}:')
        for i , g in enumerate(times[buscar]["gols"]):
            print(f'    para {i+1}ª partida foi feito {g} gols.')
    print('-' * 40)
print(' Volte Sempre ')


# ------- Comentarios do codigo --------------- # 

# criado uma lista chamada times()

# criado um laço while true:
    # contendo todo o conteudo do desafio 93 já pré produzido
    
# 