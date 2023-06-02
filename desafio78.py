#faca um programa que leia 5 valores numericos e guarde-os numa lista .
# No final mostre qual foi o maior e o menor valor digitado e suas respectivas posições 

# criando uma lista vazia
# criando variaveis para verificar o maior e o menor numero as mesmas atribuidos valores iniciais a 0
valores = []
maior = 0
menor = 0
# criando um laço para realizar a leitura dos valores pelo teclado e armazenar na lista 
    # criando um inout usando a função append para adicionar valores num intervalo pré definido que seria range(0, 5)
    # criando condiçoes if para verificar o maior e menor numero verificando sua posição no intervalo pré definido 
for c in range(0, 5):
    valores.append(int(input(f'digite um numero na posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]       
print('-=-' * 30)
print(f'A lista completa é : {valores}')
print(f'O Maior valor digitado na lista é : {maior} na posição ', end = '')
# criando um laço for para verificar as posiçoes dos valores maiores dentro da lista 
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end = '')
print()    
print(f'O Menor valor digitado na lista é : {menor} na posição ', end = '')
# criando um laço for para verificar as posições dos valores menores dentro da lista
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end = '')
print()