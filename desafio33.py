#faça um programa que leia três números e mostre qual é o maior e o menor.
a = int(input('Digite Pirmeiro número:'))
b = int(input('Digite Segundo número:'))
c = int(input('Digite Terceiro número:'))
#verificando quem é menor 
menor = a
if b<a and b<c:
  menor = b
if c<a and c<b:
  menor = c
print('-=-'*20)
print('o menor numero digitado foi:{}'.format(menor))
print('-=-'*20)
#verificando maior 
maior = a
if b>a and b>c:
  maior = b
if c>a and c>b:
  maior = c
print('-=-'*20)
print('O maior número digitado foi :{}'.format(maior))
print('-=-'*20)