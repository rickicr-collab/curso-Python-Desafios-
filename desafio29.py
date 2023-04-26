#escreva um programa que leia a velocidade de um carro.
#se ele ultrapassar 80km/h. mostre uma mensagem que ele foi multado.
#a multa vai custar 7,00 R$ por cada km acima do limite.
velocidade = float(input('Qual é a velocidade?')) # variavel velocidade para que seja indicado a velocidade 
limitador = 80 # variavel limitador que indica o valor da velocidade permitida 
if velocidade > limitador: # condição de if para o limite de velocidade e para a multa por ultrapassar o limite de velocidade
  print('MULTADO! você está acima da velocidade permitida que é 80km/h')
  multa = (velocidade-80) * 7 # variavel multa calculando o valor excedente de 80 km vezes 7 
  print('Você foi multado no valor de R${:.2f}!'.format(multa))
else: # condição de else caso vc não atenda as condições de if o programa irá acionar imediatamente o else
  print('MUITO BEM! está digirindo de forma correta')
print('Tenha um bom dia ! Dirija com cuidado')