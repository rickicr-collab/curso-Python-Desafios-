#refaça o desafio 51, lendo o primeiro termo e a razão de uma PA. mostrando os 10 primeiros termos da progresso usando a estrutura while.

print('-=-' * 10)
print(' Calculando PA ')
print('-=-' * 10)
pritermo = int(input('Digite o primeiro termo:')) # variado primeiro termo criado para informaçoes no terminal
razão = int(input('Digite a razão da PA:')) # variavel razão criada para informaçoes no terminal
termo = pritermo # variavel termo recebe a variavel termo
count = 0 # variavel count recebe o valor inicial 0
while count <= 10: # condição count é menor ou igual a 10 o while é iniciado atá atingir o valor 10 
    print('{} → '.format(termo), end='')
    termo += razão # variavel termo informada com acrescimo da variavel razão + 1
    count += 1 # variavel informada com acrescimo da variavel count + 1
print('Fim!!!')