'''Faça um programa que tenha uma função
chamada escrever(), que receba um texto
qualquer como parametro e mostre uma mensagem
com tamanho adaptavel.'''

# função para edição e apresentação de titulo
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'= {msg} = ')
    print('~' * tam)   
    

# programa Principal
escreva(' Ricardo Cunha ')


# ======== comentarios do codigo ======== #

# funççoes criadas:

# função escreva
''' criada uma função chamada escreva com paramentro: (msg)
variavel tam criada que recebe → tam = len(msg) + 4( caracteres adicionais )
criado print com caracterer divisor formatado → print('~' * tam)
criado print com parametro msg com seguintes formatações → print(f'= {msg} =')
criado print com caracterer divisor formatado → print('~' * tam)
'''

# programa principal
''' Função escreva com parametro → ( ' Ricardo Cunha ')'''