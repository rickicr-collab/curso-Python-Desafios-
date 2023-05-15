#crie um programa que leia varios numeros inteiros pelo teclado.
# O programa só vai parar quando o usuario digitar o valor 999 condição de parada
# mostrar quantos numeros foram digitados 
# mostra a soma entre eles desconsiderando o flag
numero = 0
soma = 0
cont = 0
while True:
    numero = int(input('Digite um numero (para parar digite 999):'))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'A quantidade de numeros digitados foram {cont}')
print(f'A soma dos numeros digitados foi {soma}')