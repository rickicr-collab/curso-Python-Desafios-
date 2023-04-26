#faca um programa que leia um numero de 0 a 1999 e mostre na tela cada um dos digitos separados:
# Exemplo:1834
#unidade: 4
#dezena: 3
#centena:8
#milhar:1
num = int(input('Digite um numero:'))# criando a variavel num com classe primitiva inteira
u = num // 1 % 10 # variavel u atribuida a operação de num com divisão inteira por 1 tirando o modulo da divisão usando % por 10
d = num // 10 % 10 # variavel d atribuida a operação de num com divisão inteira por 10 tirando o modulo da divisão usando % por 10
c = num // 100 % 10 # variavel c atribuida a operação de num com divisão inteira por 100 tirando o modulo da divisão usando % por 10
m = num // 1000 % 10 # variavel m atribuida a operação de num com divisão inteira por 1000 tirando o modulo da divisão usando % por 10
print('Analisando o numero {}'.format(num))
print('Unidade:{}'.format(u)) #imprimir o valor da operaçao da variavel u
print('Dezena:{}'.format(d)) #imprimir o valor da operação da variavel d
print('Centena:{}'.format(c)) #imprimir o valor da operação da variavel c
print('Milhar:{}'.format(m)) #imprimir o valor da operação da variavel m