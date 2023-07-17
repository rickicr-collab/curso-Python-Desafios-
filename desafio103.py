''' Faça um programa que tenha uma função
chamada ficha(), que recebe dois parametros
opçionais: o nome de um jogador e quantos gols ele marcou

o programa deverá ser capaz de mostrar
a ficha do jogador, mesmo que algum dado não tenha sido informado
corretamente'''


def titulo(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f' {msg}')
    print('-' * tam)


# função criada ficha
def ficha(jog = '<Desconhecido>', gol = 0):
    """_summary_
    -> armazena os dados e mostra na tela 
    Args:
        jog (_type_): variavel jogador tipo string
        gol (_type_): variavel gol tipo int
    """
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')


#programa Principal
titulo(f' {" Ficha Jogador "}')
n = str(input('Digite o nome do jogador:'))
g = str(input('Quantidade de Gols'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n, g)    
    


# ========= comentarios ========= #

# criado função titulo
    ''' para estiliza criando um titulo inicial para exibiçao
    do programa principal '''

# criada função ficha
    ''' com parametros opçionais sendo eles:
    jog = 'Desconhecido' → se nenhum parametro for inserido
    gol = 0 → se nenhum valor for inserido
    print formatado informando o nome e a quantidade de gols registrada'''
    
# programa principal 
    # criada variavel n → com input para ser inserido valores pelo teclado
    # criado variavel g → com input para ser inserido valores pelo teclado

# criado condição if:
    # onde se g é um numero.
    ''' a variavel g → irá receber o valor inteiro de g = int(g)'''
    # se g não é numerico:
    ''' a variavel g → irá receber o valor zero = g = 0'''
    
# criado condição if:
    # onde se variavel n usando função strip() recebe paramentros vazios → n.strip == '':
    '''Usando a função ficha() o parametro gol recebe g →  ficha(gol = g)'''
    # se a condição if não for atendida:
    '''Usando a função ficha() que recebe os parametros → ficha(n, g)'''