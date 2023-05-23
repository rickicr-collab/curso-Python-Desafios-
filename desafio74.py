# crie um programa que vai gerar cinco numeros aleatorios e colocar em uma ordem tupla.
# depois disso , mostre a listagem de numeros gerados e tambem indique a menor e a maior valor que estão na tupla 

from random import randint  # importando o metoro randint da bliblioteca random

numeros = (randint(1, 10), randint(1,10), randint(1, 10),
           randint(1, 10), randint(1, 10)) # usando o metodo randint é gerado um numero aleatoriro entre os intervalos 1 a 10(criando cinco numeros randomizados na mesma variavel e tupla)
print('-=-' * 16)
print(f'Os numeros sorteados foram: {numeros}')
print(f'O maior numero sorteado foi: {max(numeros)}') # usando a função nativa das tuplas chamado max é possivel extrair o maior valor das tuplas e exibilo na tela usando a função print
print(f'O menor numero sorteado foi: {min(numeros)} ') # usando a função nativa das tuplas chamada min é possivel extrair o maior valor das tuplas e exibila na tela usando a função print
print('-=-' * 16)