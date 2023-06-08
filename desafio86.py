# crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado:
# no final mostre a matriz na tela com a formatação correta

# ------------------- Resolução ---------------------------#
# Criando matriz vazia
    # com treis matrizes vazias internas 
    # com cada uma das treis matrizes internas com valores pré definidos zero = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Criado um laço for:
    # com condição em linha para um range pré definido de (0, 3)
    # com um nova condição para coluna com um range pré definido de (0, 3) 
    # usando a listz matriz com parametros[l][c] dentro do laço como fundamentos atravez do input para ser inseridos valores pelo teclado usando um f'string' para indentificar linha e coluna da posiçõa de cada valor inserido pelo teclado   
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor na posição → [{l}, {c}]:'))

# Criado um print de caracteres para dermacar o resultado do laço inserido na parte superior
# criado um laço for para exibição da matriz ordenada e organizada:
    # com condição em linha para um range pré deficnido de (0, 3)
    # com uma nova condição para coluna com um range pré definido de (0, 3)
    # criando um print formatado mostrando os valores informados no input do laço anterior como formatdo de matriz ordendado por linhas e colunas com 3x3 - padrão normal de matriz 
    # criando um print () vazio na mesma linha posiçõa que o segundo for para que haja a quebra de linha mais mantenha na posição de colunas ordenadas 
    
print('-=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()