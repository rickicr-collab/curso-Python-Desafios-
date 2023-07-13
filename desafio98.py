''' Faça um programa que tenha uma função 
chamada contador(), que receba três parametros :
inicio, fim e passo e realize a contagem.

Sey programa tem que realizar três contagens
atraves da função criada.

(a) - de 1 até 10, de 1 em 1
(b) - de 10 até 0, de 2 em 2
(c) - Uma contagem Persoanlizada'''

from time import sleep

def titulo(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f' {msg}')
    print('-' * tam)
    

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} com intervalos de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} → ', end = '', flush = True)
            sleep(0.6)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} → ', end = '', flush = True)
            sleep(0.6)
            cont -= p
        print('Fim!')
            
    

# programa Principal   
contador(1, 10, 1)  
contador(10,-1, 2)
titulo('Contagem Personalizada!')
ini = int(input('Digite o Inicio:')) 
fim = int(input('Digite Fim:')) 
Pass = int(input('Digite o Passo:'))
contador(ini, fim, Pass)

# importando bliblioteca time com modulo sleep

# criado função titulo
    # criando variavel tam que recebe o tamanho do parametro declarado msg
    # criado print contendo caracteres vezes a varavel tam
    # criado print contendo a mesagem que recebe o parametro msg
    # criado print contendo caraceteres vezes a variavel tam

# criando função contador
    # criando condição if → se o valor de p é menor que 0
        # então recebe o valor de p *= -1
    # criando outra condição if → se p for igual a 0
        # então p passa a receber o valor de 1 → p = 1
    
    #criando a condição if → se inicio é menor que fim → i < f
        #atribuindo variavel cont a i → cont = i
        # criaddo laço while → se cont for menor ou igual a f → while cont <= f
            #criado um print formatado informando o valor de cont, mantendo a quebra de linha , e usando a função flush que recebe valor True
            # cont recebe valores contabilizados do passo → cont += p
        # print finalizador do laço
    #criado a condição else para o valor inverso do if
    
'''função flush → referente a atualização do python que causa erro ao utilizar 
    a função sleep devido ao interpretedor bufferizar a função mais não exibir 
    em tela no tempo correto.Essa função permite que a função sleep funcionae 
    de forma normalizada na linha a ser aplicada ''' 
    