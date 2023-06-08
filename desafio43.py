# desenvvolva uma logica que leia o peso e altura de uma pessoa e calcule seu imc e mostre seu status de acordo com a tabela abaixo
# abaixo de 18.5 abaixo do peso
# entre 18.5 e 25 - peso ideial
# 25 ate 30 - sobrepeso
# 30 até 40 - obesidade
# acima de 40 - obesidade morbida
from time import sleep
('-=-' * 20)
print('Programa para calculos de IMC ')
('-=-' * 20)
candidato = input('Nome do candidato:').capitalize()
peso = float(input('Digite o peso do candidato:'))
altura = float(input('Digite a altura do candidato:'))
imc = peso / (altura * altura) 
print('Processando............')
sleep(5)
if imc < 18.5:
    print('Candidato {}\nPossui peso {} kg\naltura {} m \nPossui IMC : {:.2f} kg/m2 você está ABAIXO DO PESO IDEAL'.format(candidato, peso, altura, imc))
elif (imc >= 18.5) and (imc <= 25):
    print('Candidato {}\nPossui peso {} kg\naltura {} m \nPossui IMC : {:.2f} kg/m2 você está no PESO IDEAL PARABENS'.format(candidato, peso, altura, imc))
elif (imc > 25) and (imc <= 30):
    print('Candidato {}\nPossui peso {} kg\naltura {} m \nPossui IMC : {:.2f} kg/m2 você está no SOBREPESO'.format(candidato, peso, altura, imc))
elif (imc > 30) and (imc <= 40):
    print('Candidato {}\nPossui peso {} kg\naltura {} m \nPossui IMC : {:.2f} kg/m2 você está na OBESIDADE'.format(candidato, peso, altura, imc))
elif (imc > 40):
    print('Candidato {}\nPossui peso {} kg\naltura {} m \nPossui IMC : {:.2f} kg/m2 você está na OBESIDADE MORBIDA'.format(candidato, peso, altura, imc))
  
