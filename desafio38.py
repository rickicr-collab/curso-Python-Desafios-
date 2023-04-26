#escreva um programa que leia dois numeros inteiros e compare-os , mostrando na tela a mensagem 
#- o primeiro numero é maior
#o segundo numero é maior
#não existe valor maior os dois são iguais 
numero1 = int(input('Digite o primeiro numero:')) # variavel numero1 criada com classe primitiva inteiro por ser numero
numero2 = int(input('Digite o segundo numero:')) # variavel numero2 criada com classe primitiva inteiro por ser numero

if numero1 > numero2: # condição if informando que variavel numero1 é maior que variavel numero2
  print('O primeiro numero é maior')
elif numero1 < numero2: # condição elif informando que variavel numero1 é menor que variavel numero2
  print('O segundo numero é maior')
elif numero1 == numero2: # condição elif informando que as variaveis possuem valores iguais 
  print('Não existe valor maior os dois são iguais')
  