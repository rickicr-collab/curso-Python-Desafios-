#a confederação nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria , de acordo com a idade:
#ate 9 anos - mirim
#até 14 anos - infantil
#até 19 anos - junior
#até 20 anos - senior 
#acima - master
from datetime import date

participante = input('nome da criança:')
nascimento = int(input('Qual ano de nascimento da criança:'))
atual = date.today().year
idade = atual - nascimento

if idade <= 9:
  print('O participante de nome{} com idade {} anos,  se enquadra na categoria mirin'.format(participante, idade))
elif idade <=14:
  print('O participante de nome {} com idade {} anos, se enquadra na categoria infantil').format(participante, idade)
elif idade <= 19:
  print('O participante de nome {} com idade {} anos, se enquadra na categoria junio'.format(participante, idade))
elif idade <= 20:
  print('O participante de nome {} com idade {} anos, se enquadra na categoria senior'.format(participante, idade))
else:
  print('O participante de nome {} com idade {} anos, se enquadra na categoria master'.format(participante, idade))
  