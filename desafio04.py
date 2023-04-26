# crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis
# Desafio 04
y = input('Digite Algo:')# variavel Y criada atraves da propriedade input
print(y)# imprimir o valor Y 
print('Ele é alfabetico: ', y.isalpha()) # imprimir se o valor y  informado é alfabetico/ se não será atribuido FALSE 
print('Seu tipo primitivo é: ', type(y)) # imprimir qual o tipo de classe o valor informado em y / se não será atribuido FALSE 
print('Ele é do tipo numerico: ', y.isnumeric()) # imprimir se o valor de y é numerico/ se não sera atribuido FALSE 
print('Ele é um digito: ', y.isdigit()) # imprimir se o valor y é um digito / se nao será atribuido FALSE
print('A primeira letra é maiuscula:', y.isupper()) # imorimir TRUE se o valor de Y possui alguma letra maiuscula / se não sera FALSE
print('Ele é um espaço:',y.isspace()) # imprimir TRUE se o valor de y for um espaço / se não será atribuido FALSE 
print('Ele tem letra minuscula: ',y.islower()) #imprimi se o valor atribuido a y tiver letra minuscula / se não será atribuido FALSE
print('Ele é alfanumerico: ', y.isalnum()) #imprimi se o valor atribuido a y for alfanumerico / se diferente será atribuido o valor FALSe 
print('Ela esta capitalizada:',y.istitle()) #imprimi se o valor de y for valor capitalizado / se não será atribuido o valor FALSE 