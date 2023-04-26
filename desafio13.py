#-----------------Desafio 13----------------------#
#crie um programa para realizar o aumento de salario de um funcionário realizando um aumento com valor de taxa de 15% no valor final.
#calcular o aumento de valores usando porcetagem 
#opção 01
S = float(input('Salario Atual: R$'))
print(f'Salario + 15% = R${S*1.15:.2f}')

#opção alternativa do programa com poucas alteracoes e uma linha a mais no codigo devido a criação da variavel aumento para receber as operações necessacrias para realização do programa 
#opção 02
salário = float(input('Digite seu salario do funcionário aqui?: R$'))
aumento = salário + (salário * 15 / 100)
print('O funcionario com salario R${}, com aumento de 15% possuirá salario de: R${}'.format(salário, aumento))
#--------------------------------------------------------------