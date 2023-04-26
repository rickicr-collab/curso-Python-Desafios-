#crie um programa que leia um numero inteiro e mostre na tela se ele é impar ou par .
numero = int(input('Me diga um numero qualquer?'))
resultado = numero % 2 # variavel resultado criada para realizar a operação com numero divisiveis por dois com o resto sendo zero será PAR
if resultado == 0: # condição de IF sendo PAR
  print('o numero {} é PAR'.format(numero)) # impressão se a condição if for alcancada 
else:
  print('O numero {} é IMPAR'.format(numero)) # impressão se a condição else for alcancada