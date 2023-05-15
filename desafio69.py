# Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada , o programa deverá perguntar se o usuario quer ou não continuar no finla mostre:
# (A) - quantas pessoas tem mais de 18 anos 
# (B) - quantos homens foram cadastrados 
# (C) - quantas mulheres tem menos de 20 anos
from time import sleep 
print('-=-' * 12)
print('Cadastro Pessoas')
print('-=-' * 12)
cont18 = quanthomem = mulhermenor20 =  0
while True:
    idade = int(input('idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo: [M/F]')).strip().upper()
    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        quanthomem += 1
    if sexo == 'F' and idade < 20:
        mulhermenor20 += 1   
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar: [S/N]')).strip().upper()
    if resp == 'N':
        break
print('Processando...')
sleep(5)
print(f'Existem {cont18} pessoas cadastradas maiores de idade.')
print(f'Existem {quanthomem} Homens cadastrados.')
print(f'Existem {mulhermenor20} mulheres cadastradas com menos de 20 anos ')
