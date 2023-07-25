'''
Faça um mini-sistema que utilize
o interactive help do python. O usuario
vai digitar o comando e o manual vai aparecer 
quando o usuario digitar a palavra 'fim' , o 
programa se encerrará 

OBS: use cores
'''


from time import sleep

c = ( '\033[m',        # - 0 sem cor
      '\033[0;30;41m', # - 1 vermelho
      '\033[0;30;42m', # - 2 verde
      '\033[0;30;43m', # - 3 amarelo
      '\033[0;30;44m', # - 4 azul
      '\033[0;30;45m', # - 5 roxo
      '\033[7;30m',    # - 6 branco
    );


def ajuda(com):
    titulo(f'Acessando o manual do comando {com} \'{com}\'', 4)
    print()
    print(c[6], end = '')
    help(com)
    print(c[0], end = '')
    sleep(2)


def titulo(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end = '')
    print('~' * tam)
    print(f'  { msg }  ')
    print('~' * tam)
    print(c[0], end = '')
    sleep(1)
    
    
# programa principal 
comando = ''
while True:
    titulo('Função Ajuda PyHelp', 2)
    print()
    comando = str(input(' Função ou Bliblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo(' Até Logo ', 1)
print()


# ========= comentarios do codigo =========== #

# variaveis criadas

# variavel c
''' variavel c criada contendo codigos caracteres para formatação de cores de fundo com detalhes 
    dentro do codigo para cada cor e seu código
'''
    
# funções criadas

# função ajuda

'''criada função ajuda com parametro : (com)
   criado titulo para ordenalizar as funçoes a
   serem solicitadas dentro do terminal ao iniciar a busca
   → função help usando parametro (com) = help(com)
'''

# função titulo

''' função criada para estilizar o programa na incicialização
    contendo codificação de cores de fundo em sua estrutura sendo
    opcional o estilo utilizado
'''

# programa principal

''' criada variavel comando como string vazia
    criada laço infinito true:
        → função titulo como nome definido utilizando com na posição 2
        print com valor vazio
        variavel comando recebe input como string com valor a ser digitado no teclado
        criado condição if → if comando.upper() == 'FIM':
            a função é finalizada usando a função break
        quando a condição else é atendida:
            usando a função ajuda com paramentro variavel (comando)
'''   
