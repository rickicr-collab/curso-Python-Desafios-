#crie um programa que leia dois valores e mostre um menu na tela:
# [1]somar
#[2]multiplicar
#[3]maior
#[4]novos números
#[5]sair do programa
#seu programa devera realizar a operação solicitada em cada caso
from time import sleep 
print('Por favor insira novos numeros para iniciar o programa')
num1 = int(input('Digite o primeiro numero:'))
num2 = int(input('Digite o segundo numero:'))
seletor = 0
print('Inicializando Programa...')
sleep(5)
while seletor != 6:
    print('-=-' * 18)
    print(''' === Programa teste === ''')
    print(''' Selecione uma dessas opções
    [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Subtração
    [ 4 ] - Maior 
    [ 5 ] - Novos Numeros
    [ 6 ] - Sair do programa''')
    seletor = int(input('Escolha uma opçção:'))
    print('-=-' * 18)
    if seletor == 1: # seletor igual 1 com caracteristicas realizando a soma dos valores inseriodos 
        soma = num1 + num2
        print('A soma de {} + {} teve resultado {}.'.format(num1, num2, soma))
    elif seletor == 2: # seletor igual 2 com caracteristicas realizando a multiplicação dos valores inseridos
        multiplicação = num1 * num2
        print('A multiplicação de {}  x  {} teve resultado {}.'.format(num1, num2, multiplicação))
    elif seletor == 3: # seletor igual 3 com caracteristicas realizando a subtração dos valores inseridos 
        subtração = num1 - num2
        print('A Subtração de {} - {} teve resultado {}'.format(num1, num2, subtração))   
    elif seletor == 4: # seletor igual 4 com caracteristica realizando a comparação dos maiores valores inseridos anteriorimente
        if num1 > num2:
            maior = num1
            print(' O numero {} é o numero Maior'.format(maior))
        else:
            if num2 > num1:
                maior = num2
                print(' O numero {} é o numero maior'.format(maior))
    if seletor == 5: # seletor igual 5 referente a opção de inserir novos dados para que novas operações sejam realizados
        print('Insira Novamente os numeros!')
        num1 = int(input('Digite o primeiro numero:'))
        num2 = int(input('Digite o segundo numero:')) 
    if seletor == 6: 
        print('Finalizando o programa...')
        sleep(5) 
    else:
        print('Opção Invalida, tente novamente.')
print('Volte Sempre!!')
    