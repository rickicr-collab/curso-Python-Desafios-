#escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa , o salario do comprador e em quantos anos ele vai pagar.
#calcule o valor da prestação mensal, sabendo que elea não pode exceder 30% do salario ou então o emprestimo será negado.

valor = float(input('Digite o  \033[1;34mvalor da casa\033[m:'))
salario = float(input('Digite o \033[1;34mvalor salário\033[m:'))
tempo = float(input('Digite o \033[1;34mtempo que deseja pagar\033[m:'))

periodo = tempo * 12
plano = valor/periodo

if plano > salario:
    print(f"""Infelizmente, o seu salário é \033[1;31minsuficiente\033[m para pagar a casa no tempo desejado
Não podemos te oferecer esse empréstimo
\033[7;31mValor da prestação: {plano:.2f}R$\033[m
\033[7;31mQuantia faltando p/ prestação: {periodo-salario:.2f}R$\033[m""")
  
elif plano > 0.3 * salario:
    print(f"""Infelizmente, o valor da prestação equivale a \033[1;31mmais de 30% do salário\033[m
Portanto, não podemos te oferecer esse empréstimo
\033[7;31mValor da prestação: {plano:.2f}R$\033[m
\033[7;31m% do salário que a prestação representa: {plano / salario *100:.2f}%\033[m""")
  
else:
    print(f"""\033[1;32mNão há objeções contra o seu empréstimo!\033[m
\033[42mValor da prestação: {plano:.2f}R$\033[m""")
  

