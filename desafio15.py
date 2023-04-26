#---------------Desafio 15------------------------#
#criar um programa que calcula atraves dos dias de aluguel com kilometros rodados o valor a ser pago pelo serviço com taxa de 60R$ ao dia + 0.15 R$ por kilometro rodado
#programa que simula periodo de aluguel de carros 
Dias = int(input('quantos dias alugados? '))
km = float(input('quantos km rodados? '))
preço = (Dias*60) + (km*0.15)
print('O total a se pagar R$:{:.2f}'.format(preço))
#------------------------------------------------------------------------