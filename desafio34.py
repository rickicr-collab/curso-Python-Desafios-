#escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#para salários a R$ 1.250,00 calcule um aumento de 10%
#para o inferiores ou iguais o aumento é de 15%.
from time import sleep
salário = float(input('Digite seu salario:R$'))
print('PROCESSANDO....')
sleep(3)
aumento1 = salário + (salário * 10 / 100)
if salário > 1250:
    print('O funcionario com salario {:.2f} recebeu o aumento com 10% que será: {:.2f}'.format(salário, aumento1))
aumento2 = salário + (salário * 15 / 100)
if salário < 1250:
    print('O funcionario com salario {:.2f} recebeu o aumento com 15% que será: {:.2f}'.format(salário, aumento2))