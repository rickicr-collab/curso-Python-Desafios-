# faça um programa que leia nome e peso de varias pessoas. guardando tudo em uma lista no final mostre:
# (A) - Quantas pessoas foram cadastradas 
# (B) - Uma listagem com pessoas mais Pessadas
# (c) - Uma listagem com pessoas mais leves 
# peso leve até 70 quilos 
# peso  pesado até 100 quilos 

# ----------------------------------------------------------------

# criando vriaveis e listas necessarios
    # criada lista principal classe
    # criada lista temporaria dados
    # criada variveis simples maior e menor
    
classe = list()
dados = list()
maior = menor = 0

# criado laço infinito While True:
    # usando função dados.append(str(input('Digite o nome:'))) → para registrar no teclado o nome
    # usandao função dados.append(float(input('Digite o Peso:'))) → para resgistrar no teclado o peso 
    # criado condição if para verificar o maior e menor peso registrado inicialmente
    # criado condição else para verificar a partir do valor registrado no telcado os maiores e menores valores atribuidos as variaveis maior e menor
    # adicionando os dados que foram adicionados a lista temporaria dados[] para serem copiados na lista definitiva classe[]
    # limpando a lista temporaria dados usando a função clear()
    # criando uma variavel simples chamada opção vara verificar no laço se o usuario deseja adicionar mais elementos na lista principal
    # criando uma condição if para verificar quando a variavel opção receber a string 'N' como resposta 
    # e usando a função break para quebrar o laço definitivamente ao receber a string 'N' na variavel opção 
    
while True:
    dados.append(str(input('Digite o nome:')))
    dados.append(float(input('Digite o Peso:')))
    if len(classe) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]            
    classe.append(dados[:])
    dados.clear()
    opção = str(input('Deseja continuar [S/N]:')).upper()
    if opção == 'N':
        break

# Imprimindo os dados processados 
    # imprimindo a listagem completa cadastrada
    # imprimindo o ttoal de elementos cadastrados na lista
    # imprimindo o maior peso e a listagem de pessoas com valores dos respectivos pesos maiores 
    # imprimindo o menor peso e a listagem de pessoas com valores dos respectivos pesos menores
    
print('-=-' * 30)
print(f'A lista completa cadastrada é → {classe}')
print(f'Foi cadastrado um total de {len(classe)} elementos ')
print(f'O maior peso foi registrado com {maior} kg. o Peso de ', end = '')
for p in classe:
    if p[1] == maior:
        print(f'[{p[0]}]', end = ' ')
print()
print(f'O menor peso foi registrado com {menor} kg. O peso de ', end = '')
for p in classe:
    if p[1] == menor:
        print(f'[{p[0]}]', end = ' ')
print()