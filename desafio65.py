#crie um programa que leia varios numeros inteiros pels teclado. no final da execução , mostre a media entre todos os valores e qual foi o maior e o menor valores lidos . o programa deve perguntar ao usuarios se ele quer continuar a digitar valores.
opção = 'S'
maior = menor = media = quantidade = soma = 0
while opção in 'Ss':
    num = int(input('digite um numero:'))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opção = str(input('Qual a opção desejada [S/N]:')).upper().strip()[0]
    media = soma / quantidade
print('O maior numero foi {} e o menor numero foi {}.'.format(maior, menor)) 
print('A quantidade de numeros digitados foram {} e a media entre eles é {}.'.format(quantidade, media)) 

# --------------------------------------------
#observação = a media é calculada por media = soma dos valores / quantidade de valores 