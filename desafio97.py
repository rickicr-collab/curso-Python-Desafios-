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
escreva('Ricardo Cunha ')
