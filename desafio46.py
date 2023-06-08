#faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio indo de 10 até 0 com uma pausa de 1 segundo entre eles.
import emoji
from time import sleep
print('-=-' * 20)
print('Preparações para os fogos!!!')
print('-=-' * 20)
for i in range(10, -1, -1):
    print(i,'\U0001f64c')
    sleep(1)  
print('BUM! BUM! POOOW!!')
print('Que Comece a queima de fogos \U0001f386!!!')