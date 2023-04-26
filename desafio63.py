#escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia fin=bonacci.

num = int(input('Informe o termo:')) # criada a variavel num
termo1 = 0 # primeiro termo fin=bonacci que seria 0
termo2 = 1 # segundo termo fibonacci que seria 1
print('{} → {}'.format(termo1, termo2), end='') # imprmir os valores dos dois primeiros termos que seria 0 e 1
count = 3 # variavel count como contador com numero 3 devido a se querer saber sobre o terceiro termo que é a soma dos dois primeiros 
while count <= num: # condição while como count abaixo ou igual a o valor da variavel num
  t3 = termo1 + termo2 # operação para saber o valor do terceiro termo que seria a soma dos primeiros termos termo1 + termo2
  print(' → {}'.format(t3), end='') # imprimi o valor de t3
  termo1 = termo2 # aqui realiza a troca de valores onde termo1 torna-se t2 para que a sequencia fin=bonacci passa prosseguir até o seu termo maximo informado
  termo2 = t3 # aqui realiza a troca de valores onde termo2 torna-se t3 onde se sabe que t3 é a soma de termo1 + termo2
  count += 1 # variavel count funciona com um acrescimo de 1 para mostrar os proximos termos até a condição de while ser antendida 
print(' → FIM!!')

