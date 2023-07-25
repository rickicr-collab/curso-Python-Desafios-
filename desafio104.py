''' Crie um Programa que tenha a função 
leiaint(), que vai funcionar de forma semelhante
a função input() do python. Só que
fazendo a validação para aceitar apenas valores numericos.

Ex:
n = leiaint('Digite um numero:)'''

# ==== Primeira Forma ======== #

def leiaint(num = 0):
    if leiaint:
        num = input('Digite um numero:')
        if num.isnumeric():
            num = int(num)
            print(f'\033[0;32mO numero digitado é {num}\033[m')
        else:
            print('\033[31mERRO! - Insira apena valores numericos\033[m')
    
     
def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    
    
titulo(f' {" Função leiaint "}')
n = leiaint()

# ===== Segunda Forma ===== #

def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! - Digite apenas valores Numéricos validos.\033[m')
        if ok:
            break
    return valor

# programa principal
titulo(f' {" Função Leiaint "}')
n = leiaint('Digite um numero:')
print(f'O numero digitado foi {n}')


# ==== comentarios Primeira Forma ===== #


# função leiaint
'''criada função leiaint com paramentros: num recebendo valor opcional 0'''
'''criada condição if → if leiaint:
   criada variavel num que recebe os seguintes valores:
 → num = input('Digite um numero:) 
   criada outra condição if → if num.isnumeric():
 → num = int(num) 
   print(f'O numero digitado é {num}')
   com formatação de de cor no texto
   else:
 → realiza um print informando que o valor foi digitado erroneamente
 → com codigos de formatação de cores no texto')'''
 
# função titulo
''' Criada para produzir um texto inicial estilizando para 
    inicialização do programa '''
    
# programa principal
''' Função titulo chamada com o parametro mensagem informado:'''
''' Variavel n que recebe a função leiaint()'''

# ===== comentarios Segunda Forma ====== #

# funções
# função titulo
''' criada para produzir um texto inicial estilizando o programa ao iniciar'''

# função leiaint
''' crida função leiaint com paramentro: msg
    criada variavel ok que recebe valor booleano = False
    criao variavel valor que recebe valor inicial = 0
    criado laço infinito : While True:
          variavel n recebendo valores = str(input(paramentro = msg)) 
        → criada condição if = if n.isnumeric():
          variavel valor recebe = o valor int(n)
          a variavel ok recebe agora valor booleano = True
        → criado condição else:
          criado um print informando quando os dados digitados são invalidos (possuindo formatação de cores no texto)
        → condição if = if ok:
          realizado a quebra do laço usando a função break
    Retornando da função variavel valor'''
    
# progrmaa principal
''' função titulo recebendo o paramentro mensagem informaado no parenteses.'''
''' variavel n recebendo função valores com paramentros:
  → n = leiaint(parametro mensagem = 'digite um numero:)'''
''' print formatado informando o valor da variavel n'''