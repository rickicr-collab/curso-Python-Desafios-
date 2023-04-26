#escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversão:
#1 para binario / 2 - para octal / 3 - hexadecimal
numero = int(input('Digite um numero:')) # input com variavel numero para ser inserido 
conversor = int(input('Você deseja converter esse numero para:\n' # variavel conversor com input para seleção com quebra de linha \n
    '1) binario\n'
    '2) octal\n'
    '3) Hexadecimal\n'))
if conversor == 1: # condição if  se for selecionado a opção numero 1
  print(bin(numero))
elif conversor == 2: # condição elif se for selecionado a opção 2
  print(oct(numero))
elif conversor == 3: # condição elif se for selecionado a opção 3
  print(hex(numero))
else: # condição else opçional se nemhuma das opções do input anteriores tiver sido escolhida 
  print('escolha uma opçãoe valida.')
  
# - -------- opção 02 -----------------------------------------------

num = int(input('Digite um numero inteiro:')) # variavel numero criada 
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÀRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção:')) # input criado para selecionar a opção para conversão 
if opção == 1: # condição if para conversão do numero para binario
  print('{} convertendo para BINÀRIO é igual á {}'.format(num, bin (num)[2:].upper()))
elif opção == 2: # condição elif para conversão do numero para octal
  print('{} convertendo para OCTAL é igual a {}'.format(num, oct (num)[2:].upper()))
elif opção == 3: # condição elif para conversão do numero para hexadecimal
  print('{} convertendo para HEXADECIMAL é igual a {}'.format(num, hex (num)[2:].upper()))
else: # condição else para opção invalida colocada no terminal diferente das informadas 
  print('Opção invalida tente novamente.')
