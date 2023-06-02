# crie um prgrama onde o usuario possa digitar cinco valores numericos e cadastreos em uma lista.
# ja na posição correta sem usar a função sorte 
# no final mostre a lista ordenada na tela


# -------------------------------------------------------------------------------------------------

# criando a lista vazia 
valores = []

#  criando um laço for 
    # com um range(0, 5) considerando que na programação o valor 5 é ignoreado e é considerado apenas do 0 ao 4
    # criado a variavel n → como inout para ser inserido os valores no range especificado na condição for formatando usando f'string' para informar a posição a ser digitado o numero
    # criando uma condição if onde se o c for o primeiro na lista adicone um numero ou se o valor informado em n for maior que o valor colocado na lista então para ambas as condições adicione um numero na lista.
    # criado um print para deixar informado os numeros informados 
    # criada variavel pos = 0 
    # criada ondição else → criando um laço while varrendo a posição dentro da largura de listas
    # dentro do laço while criando uma condição if → com a posição sendo menor ou igual a posição dentro da lista
    # realizando a inserção dos valores usando a função insert(pos, n) usando como paramentros = pos → posição dentro / n → numero adicionado
    # print informando que o nuemro foi adicionado de acordo a sua posição na lista 
    # a variavel pos realiza um contador para contabilizar cada valor inserido dentro do laço wuile lembrando que esse contador está na mesma linha de nivel que a condição if dentro do laço while
    # logo apos usando a função break para quebrar o laço de repetição while
for c in range(0, 5):
    n = int(input(f'Digite um numero → na posição {c}: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if pos <= valores[pos]:
                valores.insert(pos, n)
                print(f'adicionado na posição {pos} da lista ...')
                break
            pos += 1

# print criando uma linha para finalizar o programa 
# print informando a lista completa inserida de forma ordenada dos 5 numeros digitados 
print('-=-' * 20)
print(f'os numeros foram inseridos em lista completa que é → {valores}')
