# crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista.
# caso o numero já exista na lista dentro ele não será adicionado no final serão exibidos todos os numeros unicos digitados em ordem crescente.

# ------------------------------------------------------------------------------------------------------------------------------------------------

# Criaçao de variaveis importantes 
    # lista vazia
    # variavel contador → (variavel que contabiliza a quantidade de valores digitados e o agrupa na lista no final )
    # variavel opção → criada para gerar a opção se o usuario deseja inserir novos numeros consecutivos ou encerrar a adição de novos numeros 
    # variavel n → criado para realizar a adição dos numeros na lista valores dentro do laço
valores = []
count = 0
opção = ''
n = 0

# Criação do laço while True com informações :
    # variavel n → criada para inserção no teclado dos numeros a serem adicionados a lista
    # condilçaõ if para os numeros que não foram adiconados a lista / para ser adiconados usando a função append()
    # função append → para adicionar novos valores a lista vazia usando o parametro (n)
    # variavel count → count += 1 contabilizando todos os numeros informados e registrados na lista valores
    # variavel opção atribuida a um input → para perguntar se o usuario ainda quer adicionar mais numeros ou não
    # condição if informando que opção == 'N' realizar a quebra do laço usando a função break 

while True:
    n = int(input('Digite um numero:')) 
    if n not in valores:
        valores.append(n) 
        print('Numero adicionado com sucesso...!')
    else:
        print('Numero duplicado! não pode ser adicionado')        
    count += 1
    opção = str(input('quer continuar [S/N]:')).strip().upper()
    if opção == 'N':
        break
print('-=-' * 16)
print(f'A lista completa e ordenada é → {sorted(valores)}')  