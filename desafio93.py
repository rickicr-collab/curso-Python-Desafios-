# crie um programa que gerencie a aproveitamento de um jogador de futebol. O progrma vai ler o nome do jogar e quantas partidas ele jogou , Depois vai ler a quantidade de gols feitos em cada partida. No final tudo isso será guardado em um dicionario. incluindo o total de gols feitos durante o campeonato.


jogador = {}
partidas = []


print(f' {"    === Analise de jogador ===   ":^20}')
jogador['Nome'] = str(input('Nome do jogador:')).capitalize()
totaldegols = int(input(f'Quantas partidas {jogador["Nome"]} jogou ?'))
for c in range(0, totaldegols):
    partidas.append(int(input(f'   Quantos gols por partida {c+1}ª: ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)

print('-=-' * 15)
print(f' {"    === Resutado da Análise ===   ":^20}')
print(f'{"Primeiro Formato:":<20}')
print(jogador)
print()
print(f'{"Segundo Formato:":<20}')
for k, v in jogador.items():
    print(f'O [{k}] recebe → {v}')
print()
print(f'{"Terceiro Formato:":<20}')
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas')
for i, v in enumerate(jogador['Gols']):
    print(f'   → Na partida {i+1} fez tantos {v} gols.')
print(f'   → Foi um total de {jogador["Total"]} gols.')    
print('-=-' * 15)
   
# --------- comentarios ------------ #

# criado lista e dicionarios:
    # dicionarios jogador{}
    # lista partidas[]
 
# criado variavel simples chamada totaldegols que recebe valor inteiro pelo teclado usando input 
# para dicionario jogador:   
    # criado chave ['Nome'] que recebe valor pelo teclado usando input

# criaddo laço for:
    # com um contador com range (0, totaldegols):
        # usando função append para adicionar os dados pelo teclado usando input para lista pré criada partidas

# Adicionado novas chaves para dicionario Jogador:
    # chave ['Gols'] que recebe uma copia dos dados da lista partidas 
    # chave ['Total'] que recebe a soma dos valores da lista partidas
    
# imprimindo os valores de treis formas:
    # primeira forma:
        # impressão de todos os dados de dicionario jogador
    # segunda forma:
        # usando um for para cada chave e valor com função items():
            # usando um print formatado atribuido um valor para chaves(k) que recebe o valores (v)
    # Terceira Forma:
        # usando um for com indice e valores por enumerate como parametro (jogador['Gols']):
            # usando um print formatado informado para cada partida a quantidade de gols feitos pelo jogador
            # print mostrando o total de gols extraindo informação da chave ['total'] dentro de jogador 

