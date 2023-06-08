#faca um programa que calcule a soma entre todos os numero impares que são multiplos de treis e que se encontram no intervalo de 1 até 500
soma = 0
cont = 0
print('-=-' * 23)
print('Lendo a soma dos valores impares de um intervalo de 1 a 500')
print('-=-' * 23)
for n in range(1, 501, 2):
  if n % 3 == 0:
    cont = cont + 1 # função de contar numeros somando apenas 1
    soma = soma + n # função de acumular numeros somando os valores
print('A soma de todos os {} valores impares solicitados no intervalo de 1 a 500 é {}'.format(cont,soma))
  
