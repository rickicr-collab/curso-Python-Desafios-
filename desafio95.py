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

# listas e dicioanrios criados :
''' lista times criada → time = list()'''
''' dicionario jogador criado → jogador = dict()'''
''' lista partidas criada → partidas = list()'''

# criado laço While True:
''' função clear para jogador → jogador.clear()'''
''' dicionario jogador recebe chave nome atraves de input → jogador['nome'] = str(input('nome do jogador'))'''
''' variavel tot recebe valor por input → tot = int(input('Total de jogos do jogador:))'''
''' função clear para partidas → partidas.clear()'''
    # criado laço for com contador in range comparamentros (0, tot) → for c in range(0, tot):
'''função append para partidas atraves de um input → partidas.append(int(input(total de gols por partida com formatação de ordem para elas)))'''
'''dicionario jogador recebe chave gols de copia de partida → jogador['gols'] = partida[:]'''
'''dicionario jogador recebe chave totals que é a soma das partidas → jogador['totals'] = sum(partidas)'''
'''é realizado uma copia e adicionado a lista times os dados de jogador → times.append(jogador.copy())'''
    # criado laço while True:
''' criado variavel resp com dados por input com formatações de string na linha de cod → resp str(input(deseja continuar? [S/N]:)).upper()[0]'''
        #criado condição if → if resp in 'SN':
'''Sai do laço atual usando a função break'''
'''realiza um print se caracteres diferente for utilizado na função input da condição if acima → print(ERRO! → digite apenas opções S ou N)'''
    # criado condição if sendo → if resp =='N':
''' quando a variavel receber o valor N como parametro no teclado é realizado a quebra do laço Pai e saindo completamente do codigo usando a funçao break'''

# da linha 25 a linha 36:
''' Realizado laços for para organizar e estilizar o codigo informando os valores contidos dentro do dicionario que foi copiato para a lista times '''

# criado laço While:
''' criado variavel buscar onde atraves dos dados organizados anteriormente e estilizados dentro das linhas de intervalo 25 a 36 para serem visualizados mais detalhadamente
  → buscar = int(input('Mostrar dados de qual jogador? ( digite 999 para parar))) com condição de numeração 999 para encerrar o cod e o programa'''
    # criada condição if → if resp == '999':
''' quando o input da variavel buscar recebe o valor 999 é realizado a quebra do laço e o fim do cod usando a função break'''
    # criado condição if → if buscar >= len(times):
''' quando a variavel buscar recebe um valor que esta acima do total armazenado no tamnho da lista times é mostrado em tela um print sendo 
  → print(ERRO! - Não dados do jogador com {buscar} digitado na busca)'''
    # criado condição else:
''' realizado um print mostrando a seguinte mensagem → print(f'Levantamento do jogador{times[buscar]['nome']}:')'''
        # criado laço for → for i, g enumerate(times[buscar]['gols']):
''' realizado um print mostrando os seguintes dados → print(f'   para {i+1}ª partida foi feito {g} gol(s))'''