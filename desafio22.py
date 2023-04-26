#crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiusculas 
# o nome com todas as letras minusculas 
# quantas letras ao todo sem considerar os espacos 
# quantas letras tem o primeiro nome?
from time import sleep
nome = str(input('Digite seu nome: ')).strip() #aplicando a propriedade .strip diretamente na variavel 
print('Avaliando seu nome....')
sleep(3)
print('Seu nome completo em maiusculo é:{}'.format(nome.upper())) # função .upper realizando a função de tornar todos os caracteres em maiusculo
print('seu nome completo em minusculo é:{}'.format(nome.lower())) # função .lower realizando a função de tornar todos os caracteres em minusculo
print('O numero total de letras do nome é:{}'.format(len(nome) - nome.count(' '))) # função len realizando a leitura e função count retirando o espacos entre as palavras 
print('seu primeiro nome tem : {} letras'.format(nome.find(' ')))
separa = nome.split() # criado variavel separa aplicando a função nome.split() criando uma lista
print(separa) # imprimindo variavel separa  
print('seu primeiro nome é {} e ele tem: {} letras'.format(separa[0], len(separa[0])))#imprimindo o primeiro nome juntamente com a total de letras do primeiro nome usando função len(separa[0])) destacando a posição na lista do primeiro nome usado com a função split
