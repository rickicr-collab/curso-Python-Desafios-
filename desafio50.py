#desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares . se o valor digitado for impar. desconsiderar 
soma = 0 # atribuido o valor zero para acumulador soma 
cont = 0 # atribuido o valor zero para contador 
for c in range(1, 7): # intervalo de 6 numero inteiros 
  num = int(input('Digite um numero:')) # criando um input para se escrever seis numeros inteiros aleatorios 
  if num % 2 == 0: # dentro do laço da variavel num condição especifica apenas para numeros pares
    cont = cont + 1 # realizar a contagem de valores pares
    soma = soma + num # realizar soma acumuladora dos valores pares declarados no if dentro do laço
print(' Você informou {} numeros e a soma entre numeros pares foi {}'.format(cont, soma))