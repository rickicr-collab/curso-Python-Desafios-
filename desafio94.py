#crie um programa que leia nome, sexo e idade de varias pessoas e guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista . no final mostre:
# (A) - Quantas pessoas foram cadastradas
# (B) - A média de idade dos grupos.
# (C) - Um alista com todas as mulheres
# (D) - Uma lista com todas as pessoas com idades acima da media 


pessoas = []
cadastro = {}

soma = media = 0

while True:
    cadastro['nome'] = str(input('Digite o nome:')).capitalize()
    while True:
        cadastro['sexo'] = str(input('Digite o sexo [F/M]')).upper()[0]
        if cadastro['sexo'] in 'FM':
            break
        print('ERRO! - digite apenas as opções S ou N no telcado.')
    cadastro['idade'] = int(input('Digite a idade:'))
    soma += cadastro['idade']
    pessoas.append(cadastro.copy())
    cadastro.clear()
    while True:
        resp = str(input('Deseja continuar? [S/N]:')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! - Digite apenas as opções S ou N no teclado.')
    if resp == 'N':
        break
    
print('-=-' * 15)
media = soma / len(pessoas)
print(f'{" === Analise de Dados === ":<20}')
print(f'(A) - A quantidade de pessoas cadastradas é : {len(pessoas)}')
print(f'(B) - A média de soma das idade é {media:5.2f} anos.')
print('(C) - O lista de nomes das mulheres cadastradas são', end = ' ')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'[{p["nome"]}]', end = ' ')
print()
print('(D) - Lista de pessoas com idade acima da media são :')
for p in pessoas:
    if p['idade'] <= media:
        for k,v in p.items():
            print(f' - [{k}] = {v};', end = ' ')
        print()
                
        
# ----- comentario do codigo ----------#

# criado lista → pessoas
# criado diçionario → cadstro
# criado variaveis 
    # variavel soma 
    # variavel media
    
# criado laço while True:
    # criada chave nome → recebendo um input string para ser inserido dados no teclado
    # criado outro laço while  True:
        # criado chave sexo → recebendo um input string para ser inserido dados pelo teclado
        #criando condição if para valor a ser inserido no teclado na chave sexo pelo input :
            # sair do laço criado usando função break
        #Criado um print informando sobre dados invalidos inseridos no teclado na chave sexo criada
    # criada chave idade → que recede um input inteiro para ser inserido dados no telcado
    # variavel soma recebe os dados acumulativos do valor idade inserido no tecladocomo contador
    # Usando a função append para adicionar os dados criados no dicionario cadastro para lista pessoas usando a função secundaria interna dos dicionarios copy()
    # apos a copia dos dados usando a função clear() no dicionario cadstro para não haver conflitos de dados na impressão
    # criado outro laço while True:
        # criada variavel resp → que recebe input string para ser inseriod dados no teclado
        # criando condição if para verificar se os dados inseridos existe dentro da variavel resp dentro do laço .
            # ao verificar se a condição anterior for verdadeira é realizada a quebra do laço  usando a função break

# a variavel media → recebe o valor acumulado da variavel soma dividido pelo tamanho de valores existentes dentro da lista pessoas 

# imprimindo a condição A do desafio → informando sobre a quantidade de dados cadastrados no dicionario e depois copiados para lista
# imprimindo a condição B do desafio → informanddo a media de idade dos pessas cadastradas no dicionario de depois copiados para lista 
# criado um print para condição C do desafio com informaçoes :
# criado um laço for:
        # para verificar na lista pessoaas:
            # para cada mulher cadastrada imprima os nomes dela - usando um print formatado 
        
# criado um print para condição D do sesafio com informaçoes para pessoas com idade acima da media:
# criado um laço for:
    # criado condição for para verificar se a idade é menor ou igual ao valor verificado pela variavel pre criada anteriormente chamada (media):
        # criado outro laço for verificando k,v dentro da função items()
            #imprimindo as chaves para seus respectivos valores verificando a condição de pessoas com idade acima da média 