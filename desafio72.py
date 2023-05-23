# crie um programa que tenha um a tupla totalmente preenchida com uma contagem por extensão de zero até vinte.
# seu programa deverá ler um numero de teclado e mostralo por extenso
cont = ('Zero', 'Um', 'Dois', 'Três','Quatro',
        'Cinco','Seis','Sete','Oito','Nove',
        'Dez','Onze','Doze','Treze','Quatorze',
        'Quinze','Dezesseis','Dezessete','Dezpito',
        'Dezenove','Vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('tente novamente.', end = '')
print(f'Você digitou o numero {cont[num]}')