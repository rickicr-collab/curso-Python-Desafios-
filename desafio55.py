#Faca um programa que leia o peso de cinco pessoas no final mostre qual foi o maior e menor pesos lidos 
maior = 0
menor = 0
for p in range(1, 6):
  peso = float(input('Qual o peso da {}º pessoa :kg '.format(p)))
  if p == 1:
    maior = peso
    menor = peso
  else:
    if peso > maior:
      maior = peso
    if peso < menor:
      menor = peso
print('-=-' * 20)
print('\033[31m O maior peso lido foi de {}Kg\033[m '.format(maior))
print('\033[32m O menor peso lido foi de {}kg\033[m '.format(menor))
print('-=-' * 20)
