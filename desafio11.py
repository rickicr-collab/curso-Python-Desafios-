
#--------Desafio 11-----------------------#
#crie um programa onde possuindo a altura e largura ambas sejas visualizadas na tela e juntamente calculado a quantidade em litros de tinta necessarios para realizar a pintura dessa mesma parede com essas medições 
#calcular valores metricos 
a = float(input('Qual a altura da parede: '))
l = float(input('Qual a largura da parede:'))
M = a*l
t = (a*l)/2
print('Você vai precisar de:{} litros de tinta'.format(t))

# opção alternativa de realizar o programa alteraçoes minimas nos codigos 
#opção 02
larg = float(input('Digite a Largura da parede: '))
alt = float(input('digite a altura da parede: '))
area = larg * alt
print('Sua parede tem as dimensoes de {:.2f} x {:.2f} sua area será {:.2f}m²'.format(larg, alt, area))
tinta = area/2
print('para pintar essa parede, você precisa de: {:.2f}litros de tinta'.format(tinta))