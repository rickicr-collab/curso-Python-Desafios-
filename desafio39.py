#faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sa idade :
# SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR 
#SE É HORA DE SE ALISTAR 
#SE JA PASSOU DO TEMPO DO ALISTAMENTO
# Sseu programa tambem deverá mostrar o tempo que falta ou se passou do prazo 
from datetime import date
atual = date.today().year
nascimento = int(input('Qual ano de nascimento?'))
idade = atual - nascimento
print('Quem nasceu {} tem {} anos em {}'.format(nascimento,idade, atual))
if idade == 18:
    print('\033[1;33mVocê esta com {} anos se aliste Imediatamente!\033[m '.format(idade))
elif idade < 18:
    saldo = 18 - idade
    print('\033[1;32mAinda falta {} anos para o alistmento !\033[m'.format(saldo))
    ano = atual + saldo
    print('\033[1;32mSeu alistamento será {}\033[m'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('\033[1;31mVocê ja deveria ter se alistado a {} anos !!!\033[m '.format(saldo))
    alistamento = atual - 18
    print('\033[1;31mseu alistamento foi em {}\033[m'.format(alistamento))
  










