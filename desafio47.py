#crie um programa que mostre na tela todos os numero pares que estão no intervalo entre 1 e 50
print('-=-' * 25)
print('Programa mostrando numeros pares num intervalo de 1 a 50')
print('-=-' * 25)
for i in range(1, 51):
    print('.', end='')
    if i % 2 == 0:
        print(i, end=' ');
print('Acabou!!')
