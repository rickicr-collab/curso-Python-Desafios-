#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.
cid = str(input('Qual cidade você nasceu?')).strip() #criada a variavel cid com classe primitiva string aplicando a função .strip para eliminar espacos desnecessarios 
print(cid[:5].capitalize() == 'Santo') # imprimir as informaçoes da variavel de cid realizando função .capitalize() igualando a string 'Santo e verificando se a mesma existe na frase colocada no terminal.  
