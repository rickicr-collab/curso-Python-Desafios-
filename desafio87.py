''' Aprimore o desafio anterior mostrando no final :
(A) - A soma de todos os valores pares digitados
(B) - A soma dos valores da terceira coluna
(C) - O maior valor da segunda linha''' 


# --------------- Resolução ---------------------#

# criado matriz principal com treis matrizes internas pré criadas 
# criado treis variaveis simples 
    # Variavel somapar → para realiza a soma dos elementos pares inseridos na matriz
    # variavel maior → para verificar qual o maior valor digitado na segunda linha 
    # variavel somacol → para verificar a soma dos valores da terceira coluna 
    
# criado um laço for:
    # criando uma condição de para linha com range (0, 3)
    # criando uma condição para coluna com range (0, 3)
    # criando um input para adicionar valores a lista vazeia matriz de acordo com a linha usando um f'string' para indentificar a localização dos valores dentro de cada matriz interna criada anteriormente 
    
# criado um laço for:
    # criando uma condição para linhas e colunas com range de (0, 3)
    # criando um print formatado informando os valores de linhas e colunas com formatação de 5 caracteres para cada valor dde forma centralizada para organizar os valores , incluindo um end='' para que a valores da mesma linha seja mantidos e apenas os valores da proxima linha realizem a quebra de paginas mantendo o mesmo principio da linha anterior.
    # criando uma condição if para veirificar se cada valor dentro das linhas e colunas é valor par.
        # então a variavel somapar = recebe a soma dos valores em cada linha e coluna existente na matriz e aramazena na mesma o valor final 
    # com isso é realizado um print formatado informando a soma dos valores pares existentes na matriz.
    
# criado laço for:
    # com condição para linha em um range (0, 3)
        # a variavel somacol = recebe a soma dos valores inseridos nas linhas com a segunda coluna como referencia em outras palavras a soma dos valores da terceira coluna 
    # criando um print formatado informando a soma dos valores da terceira coluna 
    
# criando um laço for:
    # para condição em colunas com range (0, 3)
        # com condição que a coluna seja igual a 0
            # a variavel maior = recebe o valor da matriz na linha [1] para cada coluna [c]
        # criando um elif para que se o valor da matriz[1][c] for > que a variavel maior
            # então a variavel maior = o valor contido na matriz[1][c]
# realizado um print formatado informando o maior valor digitado na segunda linha 

matriz = [[], [], []]
somapar = maior = somacol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor na posição → [{l}, {c}]:')))
               
print('-=-' * 30)      
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = ' ')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('-=-' * 30)
print(f'A soma dos valores pares digitados na matriz é {somapar}')
for l in range(0, 3):
    somacol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somacol}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor digitado na segunda linha é {maior}')