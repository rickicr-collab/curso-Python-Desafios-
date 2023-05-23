# desenvolva um programa que leia quatro valores pelo teclado e guarde -os em uma tupla . no final mostre:
# (A) - quantas vezes apareceu o valor 9
# (B) - Em que posição foi digitado o valor 3
# (C) - quais foram os numeros pares

# inserindo valores pelo teclado e adicionando em uma tupla 
print('-=-' * 16)
num = (int(input('Digite o primeiro numero:')), int(input('Digite o segundo numero:')),
       int(input('Digite o terceiro numero: ')), int(input('Digite o quarto numero: ')))
print('-=-' * 16)
print(f'Você criou uma tupla pelo teclado com valores: {num}')

# - Requisito (A)
# verificando quantas vezes o numero nove apareceu na tupla
# usando o methodo count dentro da tupla num 
print(f'O numero 9 apareceu {num.count(9)} vezes ')

# - Requisito (B)
# verificando em que posição o primeiro valor 3 foi digitado
# verificando a posição do valor 3 utilizando o methodo index dentro ta tupla num
# realizando uma condição if para que o programa não execute um erro a não ser inserido o numero 3 no teclado pelo o usuario
if 3 in num:
    print(f'O valor 3 foi digitado na posição {num.index(3)}ª')
else:
    print('O numero 3 não foi digitado')
# - Requisito (C)
# verificando os numeros pares dentro da tupla 
# utilizando um for para realizar um laço e indentificar os umeros pares inseridos pelo teclado na tula e imprimi-los na tela 
print('os numeros pares são:', end = ' ')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end = ' ')
        