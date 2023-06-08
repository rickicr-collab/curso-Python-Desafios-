# Crie um programa que leia  o ano de nascimento de sete pessoas . No final mostre quantas pessoas ainda não atigiram a maioridade e quantas já são maiores de 21 anos .
from datetime import date

atual = date.today().year
maior = 0
menor = 0
for pess in range(1, 8):
    nascimento = int(input('\033[1;33m Em que ano a {}° pessoa nasceu\033[m :'.format(pess)))
    idade = atual - nascimento
    if idade >= 21:
        maior += 1   
    else:
        menor += 1
print('\033[31m Ao todo tivemos {} pessoas maiores de idade\033[m '.format(maior))
print('\033[32m Ao todo tivemos {} pessoas menores de idade\033[m '.format(menor))
  
   
