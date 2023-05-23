# Crie um programa que tenha um tupla unica com nomes de produtos e seus respectivos preços na sequencia.
# No final mostre uma listagem de preços organizando os dados em forma tabular

# criando uma tupla com valores tanto inteiros quanto contendo valroes de string
listagem = ('Lapis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.99,
            'Canetas', 22.30,
            'Livros', 34.90)
print('-=-' * 13)
print(f'{"Listagem de preços":^40}') # realizando a formatação de String centralizando o texto com um numero especificos de caracteres de espaços definidos 
print('-=-' * 13)

# criando um forma de exibição tabular dos dados da tupla utilizando um for
# utilizando a formatação do print {.<30} vc realiza a formatação dentro de 30 caracteres para os valores pares dentro da tupla que são os nomes dos produtos alinhados a esquerda
# utilizando a formatação do print {:>7.2f} vc realiza a formatação dentro de 7 caracteres para os valores impares dentro da tupla que são os preços dos produtos alinhadas a direita com valores flutuantes de dois algarismos apos o ponto
# Utilizando um if colocando com como condição a posição dos valores pares dentro da tupla para exibição de forma posiçional os nomes dos produtos
# Utilizando um elif colocando como condição a posição dos valores impares dentro da tupla para exibição de forma posiçional os valroes dos prddutos como tabela de preços 
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end ='')
    elif pos % 2== 1:
        print(f' R${listagem[pos]:>7.2f}')
print('-=-' * 13)    