#-------Desafio 10------------#
#criar um programa onde você possa informar o valor em reais e comprar uma moeda estrageira seguindo seu valor de compra atuali 
#opção 01
r = float(input('Tenho na minha carteira:  R$'))
d = r/5.19
print('Posso comprar {:.2f} em dolars' .format(d))

#opção 02
# realizado como uma opção mais atribuida dois valores para moedas diferentes com cotações diferentes seguindo o mesmo principio que o primeiro caso 
real = float(input('Quanto dinheiro eu tenho na carteira?: R$'))
dolar = real/5.27
euro = real/5.65
print('-'*30)
print('Com R${:.2f} Você pode comprar em US$: {:.2f}'.format(real, dolar))
print('Com R${:.2f} Você pode comprar em €U$: {:.2f}'.format(real, euro))
print('-'*30)
