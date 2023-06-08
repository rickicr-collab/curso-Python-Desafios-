#faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo
tot = 0
núm = int(input('\033[1;33;46mDigite um número inteiro \033[m :')) # atribuido uma variavel num com classe primitiva inteira
for c in range(1, núm + 1): # criando um laço com variavel c em intervalo 1 até a variavel acrescentando +1 
    if núm % c == 0: # condição if onde variavel num divisivel pela variavel c com o resto == 0
        print('\033[34m', end=' ') # imprimir o valores primos com cores azul
        tot += 1 # aplicando uma variavel total usando como função de contagem 
    else:
        print('\033[31m', end=' ') # imprimir os valores não primos com cores vermelhas 
        print('{}'.format(c), end='') # imprimir com formatação o intervalo de em c criando um espacamento entre os valores do intervalo com ajuda da função end=''
print('\n O numero {} foi divisel {} vezes '.format(núm, tot)) # imprimindo a quantidade de vezes que o numero foi divisivel   
if tot == 2: # condição if quando o numero é divisivel por um e por ele mesmo então essa condição if é verdadeira 
    print('\033[34m Então ele é PRIMO!!\033[m ') # aqui imprimi o valor informando que ele é primo com formatação de cor em azul
else:
    print('\033[31m Ele NÂO È PRIMO!!!\033[m ') # else imprimindo o valor informando que ele não é primo com formatação de cor em vermelho