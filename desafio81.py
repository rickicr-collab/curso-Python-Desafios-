'''crie um programa que vai ler varios numeros e colocar em uma lista.
 (A) - Quantos numeros foram digitados
 (B) - A lista de valores ordenada na forma decrescente
 (C) - se o valor 5 foi digitado e está ou não na lista'''


# --------------------------------------------------------------------------------------------

# Importando o modulo sleep da bliblioteca time ( opicional)
from time import sleep
# Criação dos objetos (variaveis , listas , tuplas , dicionarios )
    # criando a lista vazia valores []
    # criando variavel opção = '' → como string
valores = []
opção = ''
# usando um print para uma apresentação do programa 
# usando função sleep(5) → com parametro d 5 segundos de atraso para simular a inicialização de um programa 
print('Inicializando o programa...')
sleep(5)

# criando um laço while:
    # criando a variavel n → como inputpara digitar os valores inteiros dentro do laço para ser armazenado dentro da lista vazia valores 
    # print informando que o elemento digitado foi adicionado com sucesso 
    # condição if informando que se o valor nigitado caso não esteja contido na lista valores:
        # seja adicionado usando o metodo valores.append(n) → parametro a ser usado para adicionar valores foi a variavel n pré definida acima como input a ser digitado pelo usuario
        # criado uma condição else caso o valor ja exista na lista valores
            # é realizado um print informando que o numero foi duplicado e não será adicionado
    # variavel opção criada inicialmente como string como forma de inserção de dados pelo teclado perguntndo se o mesmo que adicionar mais elementos a lista como resposta em string como foi pre estabelico em seu codigo / foi aplicado as funções:
        # função strip() → que ignora espaços despedicodos na linha
        # função upper() → que torna todos os caracteres informados com letra maiuscula 
    # criada condição if infirmando que se opção possuir valor == 'N' → seja realizada a quebra do lação usando a função break   
    
while True:
    n = int(input('Digite um numero:'))
    print('Numero Adicionado com sucesso...')
    if n not in valores:
        valores.append(n)
    else:
        print('numero duplicado! Não foi adicionado.')
    opção = str(input('Deseja adicionar mais ? [S/N]: ')).strip().upper()
    if opção == 'N':
        break

# criando um print para simular o efeito de finalização de um programa 
# usando função sleep(5) → simulando o atraso em 5 segundos 
# print informando que o programa está finalizado
# caracteres de linha para demarcar a finlização de um programa
# print informando quantos elementos foram digitados na lista e adicionados 
# usando a função sort(reverse=True) → realizando a ordem da lista em forma decrescente
# print mostrando a lista de forma decrescente criada anteriormente
# criando uma condição if onde se o valor 5 foi digitado e adicionado na lista valores
    # se for digitado mostra-rá a frase informando que foi digitado e adicionado a lista
    # se não irá mostra que não foi digitado e tambem não foi adicionado a lista  
       
print('finalizando o programa...')
sleep(5)
print('Programa finalizado!')
print('-=-' * 20)
print(f'A Quantidade de numeros digitados na lista foi : {len(valores)} elementos ')
valores.sort(reverse=True)
print(f'A lista ordenanda de forma decrescente é → {valores}')
if 5 in valores:
    print('O numero 5 foi adicionado na lista valores')
else:
    print('O numero 5 não foi adicionado a lista valores')