#-------------Desafio 17-------------------------#
#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa
# cria a função while que irá gerar a operação enquanto houver valores verdadeiros
 
while True:
    cato = float(input('Digite o valor do cateto oposto:'))#cria uma variavel  cateto oposto que recebe um valor com classe primitiva flutuanteou (real)
    cata = float(input('digite o valor do cateto adjacente:'))#cria uma variavel cateto adjacente que recebe um valor com classe primitiva flutuante (real)
    calc = (cato**2) + (cata**2)#cria uma variavel chamada calc onde se tem recebido valores de operações (cato**2) e (cata**2)
    hipo = calc**(1/2)#aqui é criado o variavel hipo onde recebe a variavel calc**(1/2)
    print('>'*50)
    print(' O valor da hipotenusa é: {:.2f}'.format(hipo))#aqui é imprimido o valor da hipotenusa pelo o valor da variavel (hipo)
    print('>'*50)
#-------------------------------------------------------------------
