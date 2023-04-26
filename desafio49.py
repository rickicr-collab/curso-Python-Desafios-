#refaça o desafio 9, mostrando a tabuada de um numero que o usuario escolher , so que agora utilizando o laço for 
num = int(input('Digite o numero para ver sua tabuada: ')) # criando um variavel para ver sua tabuada 
print('-=-' * 20)
for c in range(1, 11):#criando um laço for com variavel qualquer criando um intervalo especifico informado
  print('{} X {} = {}'.format(num,  c, num*c)) # interligando a variavel 'c' junto com o numero informado e aplicando a função de multiplicação entre a variavel e o numero informado se possui a tabuada desejada 
print('-=-' * 20)
  
  
  