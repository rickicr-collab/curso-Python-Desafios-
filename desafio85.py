#crie um programa onde o usuario possa digitar sete valores numericos e cadastra-los em uma lista unica que mantenha separado os valores pares e impares.
# No final mostre ambas as listas com valores ordenados de forma crescente 

# criando variaveis e listas 
    # criando a lista numeros e atribuido duas listas internas vazias a mesma 
    # criando a variavel valores para ser inserido elementos pelo teclado dentro do laço for 
numeros = [[], []]
valores = 0

# criado laço for:
    # laço for criado com range pré deficnido (1, 8)
    # variavel valores pre declarada foi colocada dentro do for como input para ser inserido valores no teclado
    # criando condição if para quando os valores forem par:
        # serem adicionados na lista interna de numeros posição [0]
    # criando condição else:
        # criando um if para quando os valores forem impar:
            # os valores serem adicionados a lista interna de numeros posição [1]
for c in range(1, 8):
    valores = int(input('Digite um numero:'))
    if valores % 2 == 0:
        numeros[0].append(valores)
    else:
        if valores % 2 == 1:
            numeros[1].append(valores)
            
# imprimindo os valores 
    # imprimindo os valores pares na lista da posição numeros[0] de forma ordenada usando a função sorted()
    # imprimindo os valores impares na lista da posição numeros[1] de forma ordenada usando a função sorted()
print('-=-' * 26)
print(f'Os numeros pares digitados são {sorted(numeros[0])}')
print(f'Os numeros impares digitados são {sorted(numeros[1])}')


