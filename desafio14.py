#---------------Desafio 14------------------------#
#crie um programa onde possa realizar a conversão de temperatura de celcius para farenheit de forma simples e imprimir esse valor em tela 
#conversão de temperatudo 

#criado a variavel C atraves da propriedade input com classe primitiva float
C = float(input('coloque a temperatura aqui °C: '))
#criada variavel F com calculos e operações para conversão de valores de tempraturas
F = ((9 * C) / 5) + 32
#imprimir o valor informado juntamente com o valor de sua conversão para farenheit de forma simples
print('a temperatura em {}°C convertida em farenheit sera:{}°F!'.format(C, F));
#------------------------------------------------------------------------------------------------