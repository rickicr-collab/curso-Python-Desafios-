#melhore o desafio 61 perguntando para o usuario se ele quer mostrar mais alguns termos. o programa encerra quando ele disser que quer 0 termos 
# codigo melhorado do exercicio anterior 
print('-=-' * 16)
print('Gerador de PA')
print('-=-' * 16)
pritermo = int(input('Digite o primeiro termo'))
razão = int(input('Digite a razão da PA:'))
termo = pritermo
count = 1
total = 0
mais = 10
print('{} →'.format(pritermo), end='')
while mais != 0: # condição while pai criada com paramentro variavel mais diferente de zero para ser atendida e iniciada
  total = total + mais # variavel total recebendo o total + variavel mais 
  while count <= total:
    termo += razão
    count += 1
    print(' {} → '.format(termo), end='')
  print('PAUSA!!')
  mais = int(input('Quantos termos você quer mostrar a mais ? ')) # variavel crianda com intuito de informar mais termos enquanto a condição while for antendida 
print('Progressão finalizada com {} de termos mostrado.'.format(total))