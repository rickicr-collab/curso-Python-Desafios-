#desanvolva um programa que pergunte a distançia de uma viagem em km.
#calcule o preço da passagem. cobrando R$ 0,50 por km para viagems até 200km
#calcule o preço da passagem. cobrando R$ 0,45 por para vaigens mais longas 
distancia = float(input('Qual é a distancia da sua viagem?'))
print('você terá uma viagem de {:.2f}km !'.format(distancia))
if distancia <= 200:
  preço1 = distancia * 0.50
  print('sua viagem de {} km  terá valor a pagar de {:.2f}'.format(distancia, preço1))
else:
  preço2 = distancia * 0.45
  print('sua viagem de {} km terá valor a pagar de {:.2f}'.format(distancia, preço2))
print('Tenha uma boa viagem! é obrigado por escolher nossa empresa')
  