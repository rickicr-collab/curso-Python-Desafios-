#Crie um programa que leia o nome é o preço de varios produtos. O programa deverá perguntar se o usuario vai continuar. no final mostre:
# (A) - qual é o total gasto na compra 
# (B) - quantos produtos custam mais de R$ 1000.
# (C) - qual é o nome do produto mais barato

totalgasto = produtosacimademil = menorpreço = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto:')).capitalize()
    preço = float(input('Preço do produto: R$'))
    cont += 1 # criando um contador 
    totalgasto += preço
    if preço > 1000: # criando condição onde o preço é acima de 1000 reais
       produtosacimademil += 1 
    if cont == 1: # criando atraves do contador a condição para achar o produto com o menor preço 
        menorpreço = preço # aqui se atribui o menor preço ao primeiro valor inserido
        barato = produto # variavael mostrado o nome do produto com o menor valor 
    else:
        if preço < menorpreço: # aqui onde se houver um valor menor que o preço ja estabelecido 
            menorpreço = preço # então ele passará a ser o novo menor preço
            barato = produto # variavel mostrando o nome do produto com o menor valor 
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja adicionar mais produtos? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('Fim do Programas'))
print(f'O valor total dos produtos será {totalgasto:.2f}')
print(f'Os produtos acima de R$ 1000.00 reais são {produtosacimademil}')
print(f'O produto com o valor mais baixo é R${menorpreço:.2f} é seu nome é {barato}')