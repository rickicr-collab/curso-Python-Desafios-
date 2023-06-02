# crie um programa que vai ler varios numeros e colocalos numa lista.
# depois disso crie duas listas extras que vão conter apenas os valores pares e os impares digitados. respectivamente.
# ao final mostre o conteudo das três listas geradas.

# -------------------------------------------------------------------------------------------------


# criação dos objetos ( listas, tuplas, variaveis e dicionarios)
    # criado lista com todos os elemnteos chamada valores = []
    # criado lista com todos os elementos pares chamada num_par = []
    # criado lista com todos os elementos ímpares chamada num_impar = []
    # criada variavel que recebe valor string vazio chamada opção = ''
    
valores = []
num_par = []
num_impar = []
opção = ''

# criado o laço while True:
    # criado variavel n → usando função input() para se inserir valores inteiros pelo teclado
    # print informado que o numero foi adicionado com sucesso
    # criando condição if onde n não esta dentro da lista valores 
        # com isto se o valor não esta dentro da lista usando função valores.append(n) será adicionado os elementos diretamente na lista usando a variavel n como parametro já que os valores serão informados atraves do input pelo usuario
    # criada condição if informando que se todo valor digitado for um valor par.
        # será adicionado usando função num_par.append(n) adicionando os valores pares dentro de uma lista pré criada usando o paramentro variavel n pois será adicionado os elementos digitado pelo usuario a partir dele 
    # criada condção if informando que se todo o valor impar. 
        # será adicionado usando função num_impar.append(n) adicionando os valores impares dentro de uma lista pré criada usando parametro variavel n pois será adicionado os elementos digitados pelo usuario a partir dele.
        
while True:
    n = int(input('Digite um numero: '))
    print('Numero adicionado com Sucesso...')
    if n not in valores:
        valores.append(n)
    if n % 2 == 0:
        num_par.append(n)
    if n % 2 == 1:
        num_impar.append(n)
    opção = str(input('Deseja adicionar mais numeros? [S/N]: ')).strip().upper()
    if opção == 'N':
        break

# criando print separador usando caracteres para sinalizar o fim do programa
# criando um print formatado mostrando lista completa
# criando um print formatado mostrando lista com valores pares 
# criando um print formatado mostrando lista com valores impares   
  
print('-=-' * 20)
print(f'Lista completa adicionada → {valores}')
print(f'Lista contendo valores pares → {num_par}')
print(f'lista contendo valores impares → {num_impar}')