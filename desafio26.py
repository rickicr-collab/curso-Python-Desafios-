#crie um programa que leia um frase pelo teclado e mostre:
#Quantas vezes aparece a letra'A'
#em que posição ela apareçe na primeira vez
#em que posição ela aparece na ultima vez 
frase = str(input('Digite uma frase:')).upper().strip() # criado variavel comm string e aplicado tambem a função .upper() e .strip()
print(' Na frase {} a letra A apareçe : {} vezes'.format(frase, frase.count('A'))) # imprimir o a frase utilizando a função .count('A)
print(' A primeira letra A aparece na posição : {}'.format(frase.find('A')+1)) #imrpimir a posição da primeira A utilizando .find('A') +1 para considerar o valor da posição como acrescentar mais 1
print(' A ultima letra A apareçe na posição : {}'.format(frase.rfind('A')+1)) #imprimir a posição da ultima letra A utilizando .rfind('A") +1 para considerar o valor da posição como acrescentar mais 1
