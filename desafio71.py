# Crie um programa que simule o funcionamento de um caixa eletronico.No inicio pergunte ao usuario qual o valor a ser sacado (numero inteiro)e o programa vai informar quantas cedulas de cada  valor seráo entregues.

# OBS. caixa possuindo cedulas de 20R$, 50R$, 10R$ e 1R$ 
print('-=-' * 10)
print('{:^30}'.format('Banco Teste'))
print('-=-' * 10)
valor = int(input('Quanto deseja sacar de valor? R$'))
total = valor
céd = 100
total_ced = 0
while True:
    if total >= céd:
        total -= céd
        total_ced += 1 
    else:
        if total_ced > 0:
            print(f'total de {total_ced} e o cédulas de R${céd}')
        elif céd == 100:
            céd = 50
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        total_ced = 0
        if total == 0:
            break
print('-=-' * 10)
print('Programa finalizado')