#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente 
#EXEMPLO
#primeironome: ANA
#ultimonome: MARIA
n = str(input('Digite seu nome completo:')).strip() # variavel string com função .strip() para retirar os espcacos da direta e esquerdas desnecessarios
nome = n.split() # variavel nome usando a função .split() para realizar a criação de uma lista 
print('Muito prazer em te conhecer!') # imprimir uma frase string de apresentação 
print('Seu primeiro nome é :{}'.format(nome[0])) # imprimiro primeiro nome realizando a busca com o valor da string do primeiro nome na lista como primeiro sempre será considerado o valor '0'
print('Seu ultimo nome é : {}'.format(nome[len(nome)-1])) # imprimir o ultimo nome realizando a função len(nome) usando a posição -1 (pois valores que não existe na string terão valores '-1')