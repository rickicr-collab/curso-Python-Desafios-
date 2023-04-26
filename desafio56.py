#Desenvolva um programa que leia o nome , idade e sexo de 4 pessoas .no final do programa mostte:
# a media de idade do grupo
# qual é o nome do homem mais velho
# quantas mulheres tem menos de 20 anos 
from time import sleep

somaidade = 0 # criada uma variavel com o objetivo de realizar a soma da idade das pessoas informadas no programa 
mediaidade = 0 # criada para gerar uma media da idade dos participantes w
maioridadehomem = 0 # criada para informar a idade do homem mais velho
nomevelho = '' # nome do homem mais velho
totmulher20 = 0 # variavel criada para contabilizar o total de mulheres com menos de 20 anos 
for p in range(1, 5):
  print('----{}ª Pessoa----'.format(p))
  print('=' * 15)
  nome = str(input('Qual o nome da pessoa:')).strip()
  idade = int(input('Qual a idade: '))
  sexo = str(input('Qual o sexo [M/F]:')).strip()
  print('=' * 15)
  somaidade += idade # realizando a soma da idade com o valores acrescentidos da idade
  if p == 1 and sexo in 'Mn': # com condição referente ao homem 
    maioridadehomem = idade
    nomevelho = nome
  if sexo in 'Mn' and idade > maioridadehomem:
    maioridadehomem = idade
    nomevelho = nome
  if sexo in 'Ff' and idade < 20: # condição referente ao mulher 
    totmulher20 += 1 # total de mulher acrescendido de valores somados com + 1   
mediaidade = somaidade / 4 # media da idade calculada com a soma da idade divido por 4 que seria o intervalo ou quantidade de pessoas a possuir a informação
print('Processando..........')
sleep(3)
print('-=-' * 20)
print('A média de idade do grupo é {}'.format(mediaidade))
print('O Homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos. '.format(totmulher20))
print('-=-' * 20)