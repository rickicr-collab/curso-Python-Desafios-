from time import sleep
print('-=-' * 20) # print uma string multiplicando com valor de 20
print('Analisador de Triangulos')
print('-=-' * 20) # print uma string multiplicando com valor de 20
segment1 = float(input('digite o valor do primeiro segmento:')) # variaveis segment1 criada com classe primitiva float
segment2 = float(input('digite o valor do segundo segmento:')) # variaveis segment2 criada com classe primitiva float
segment3 = float(input('digite o valor do terceiro segmento:')) # variaveis segment3 criada com classe primitiva float
print('Processando.......')
sleep(5) # aplicando a função opinional simulando o processamento de um processo 
if (segment1 == segment2 == segment3): # condição para mostrar um triangulo Equilatero
    print('o triangulo atende os requisitos para um triangulo Equilátero:')
elif (segment1 == segment2) or (segment1 == segment3) or (segment2 == segment3): # condição para mostrar um triangulo Isosceles 
    print('O triangulo atende os requisitos para um triangulo Isósceles')
else: # aplicando a condição else para um triangulo escaleno 
    print('O triangulo atende os requisitos para um triangulo Escaleno')