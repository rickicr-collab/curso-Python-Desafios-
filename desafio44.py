#elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento
#a vista dinheiro/cheque - 10% de desconto
#a vista no cartão - 5% de desconto
#em até 2x no cartão - preço normal
#3x ou mais no cartão - 20% de juros
from time import sleep
print('{:=^40}'.format('Lojas Ricardo'))
preço = float(input('Preço do produto: R$'))
print(''' FORMAS de PAGAMENTO
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista no cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção?'))
print('Processando............')
sleep(5)
if opção == 1: 
  total = preço - (preço * 10 / 100)
  print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
elif opção == 2:
  total = preço - (preço * 5 / 100)
  print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
elif opção == 3:
  total = preço
  parcelas = preço / 2 
  print('Sua compra no valor de R${:.2f} será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(preço, parcelas))
elif opção == 4:
  total = preço + (preço * 20 / 100)
  totalparcelas = int(input('Quantas parcelas deseja?'))
  parcelas = total / totalparcelas
  print('Sua compra será parcelada em {}x de R${:.2f}'.format(totalparcelas, parcelas))