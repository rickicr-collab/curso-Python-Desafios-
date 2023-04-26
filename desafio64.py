#Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999 que é a condição de parada . no final mostre quantos numros foram digitados e qual foi a soma entre eles desconsiderando o flag.
num = 0 # atribuida a variavel num criada o valor de 0
count = 0 # atribuido a variavel count criada o valor de 0
soma = 0 # atribuido a variavel soma criada o valor de 0
num = int(input('Digite um numero:')) # input variave num atribuido devido a uma limitação antecipada do problema futuramente corrigida
while num != 999: # condição while ondem valor inserido em num é diferente de valor atribuido 999 a condição é atendida e iniciada
  soma += num # soma recebe o acrescimo somando o valor de num
  count += 1 # count recebe um acrescimo de count + 1
  num = int(input('Digite um numero:')) # input e variavel de num colocado no fim da linha da condição while devido a correção da limitação inicial do problema posteriormente resolvido
print('Foram digitados {} numeros e sua soma é {}.'.format(count, soma)) # print com informaçoes solicidades e com devidas formatações 
print('Fim')
