#-------------Desafio 12----------------------#
#crie um programa que ele possa mostra em tela os valores de preço do produto a prazo com 5% de desconto no valor 
#valores usando desconto com porcetagem
#opção 01
p = float(input('preço do produto a prazo: R$'))
D = p*5/100 #operação para realizar o 5% de desconto no valor do produto 
print('Valor à vista:R$ {:.2f} '.format(p-D))

#alternativa para realizar o mesmo programa com alteracoes minimoas nos codigos com o mesmo principio da primeira alternativa 
#opção 02
preço = float(input('Qual é o preço do produto: R$'))
novo = preço - ( preço * 5 / 100)
print('O produto que custava R${:.2f}, estando na promoção com desconto de 5% terá valor de: R${:.2f}'.format(preço, novo));
#----------------------------------------------------------