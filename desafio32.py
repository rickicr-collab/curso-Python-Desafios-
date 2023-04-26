#faça um programa que leia o ano qualquer e informe se ele é um ano bissexto
from datetime import date # importando da bliblioteca datetime apenas a função date
ano = int(input('Que ano quer analizar? '))
if ano == 0: # atribuindo o valor de ano como = 0
  ano = date.today().year #atribuindo o valor 0 a variavel ano ele irá atribuir o ano atual datado no sistema do computador e executara a funções e condições necessarias para verificar se ele é um ano bissexto
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0: # colocado condições no if com valores AND e OR que são condições de valores booleanos 
  print('O ano de {} é BISSEXTO'.format(ano))
else: # condição else que será aplicada quando a condição do if não for atendida 
  print('O ano de {} não é BISSEXTO'.format(ano))