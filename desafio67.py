#faça um programa que mostre a tabuada de varios numeros um de cada vez , para cada valor digitado pelo usuario.
# o programa será interrompido quando o numero solicitado for nuegativo.
from time import sleep
print('Inicializando o programa...')
sleep(3)
while True:
    numero = int(input('Digite um numero para ver sua tabuada:'))
    if numero < 0:
        break
    print('-=-' * 13)
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero * c}')
    print('-=-' * 13)
print('Encerrando o programa...')
sleep(3)
print('Fim do Programa')