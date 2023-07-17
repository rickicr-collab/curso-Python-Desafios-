'''Crie um programa que tenha uma função
chamada fatorial() que receba dois parametros:
o primeiro que indique o numero a calcular e 
o outro chamado show, que será um valor lógico(opçional)
indicando se será mostrado ou não na tela o 
processo de calculo fatorial'''


# função titulo
def titulo(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f' {msg}')
    print('-' * tam)


# função fatorial
def fatorial(num, show = False):
    """_summary_
    -> Realiza o fatorial na função criada
    Args:
        num : Valor para calcular o fatorial
        show (bool, optional): parametro para exibir detalhe do fatorial. por padrão falso
    Returns:
          f: retornando o valor de fatorial e exibindo na tela
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end = ' ')
            if c > 1:
                print('x', end =' ')
            else:
                print(' = ', end = '')        
        f *= c
    return f
    
  

# programa principal
titulo(f' {" Gerador de Fatorial "}')
fator = int(input('Digite um numero:'))  
print(fatorial(fator, show=True))
print(fatorial(fator))
print('-' * 25)
help(fatorial)
print('-' * 25)

# ============= comentarios ================== #

# ============ Funções =============== #

    # criada função titulo
'''para estilizar criando um titulo inicial para
        exibição no programa inicial'''

    # criado função fatorial
''' com parametros opiçionais sendo eles:
    num = o valor para calcular o fatorial
    show = valor para exibir detalhes do fatorial que por padrão vem falso '''
''' criada variavel (f) que recebe → f = 1'''
    # criado condição if:
    # criado laço for com variavel c com intervalo de parametros → for c in range(num, 0, -1):
        # criado condição if → if show:
'''realizado um print → print(c, end = ' ')'''
        # condição if sendo → if c > 1:
'''realizado um print → print(' x ' , end = ' ')'''
        # criado condição else:
'''realizado  um print → print(' = ' , end = '')'''

    # f = f * c
'''realizado acumulo do valor de f sendo → f += c'''
    # return f
''' Realizando o retorno do valor de f'''
    

# ============ Programa Principal ============== #

# função titulo chamada:
'''f " {' Gerador de Fatorial '} " '''

# variavel faror que recebe input sendo → fator = int(input('Digite o valor:))

# realizado print dos resultados da função fatorial
''' fatorial do valor com parametro show = True → print(fatorial(fator, Show = True))'''
''' fatorial do valor normal sem parametro show → print(fatorial(nome))'''

# utilizando a função help para veirifcar informaçoes da função fatorial usando docstring pré criada:
''' print('-' * 25)
help(fatorial)
    print('-' * 25)
'''