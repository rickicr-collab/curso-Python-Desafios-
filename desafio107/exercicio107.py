''' crie um programa chamado 
    moeda.py que tenha as funções incorporadas
    aumentar(), diminuir(), dobro() e metade()
    
    faça tambem um programa que importe esse
    modulo e use algumas dessas funções .
'''

from moeda import dobro, aumentar, diminuir, metade

def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    
 
 
# programa principal   
titulo(f' {" Teste de Modulos "}')
valor = float(input('Digite o valor (R$):'))
print(f'O dobro do R${valor} digitado fica (R$) {dobro(valor)}')
print(f'O valor de R${valor} com 10% de aumento fica (R$) {aumentar(valor, 10)}')
print(f'O valor de R${valor} com 10% de desconto fica (R$) {diminuir(valor, 10)}')
print(f'A metade de R$ {valor} fica(R$) {metade(valor)}')


# ======== Comentarios do Codigo ========= #

# modulo e pacotes 
''' Importado modulo moeda :
    funçoes importadas → dobro, aumentar, diminuir, metade'''
    
# funçoes
''' função titulo criada para estilizar criando um
    titulo inicial para inicializar o programa '''
    
# programa principal

''' Função titulo com titulo definido no parametro'''
''' criada variavel valor com função input para digitar no teclado.
    Função print com formatação para seguintes opçoes:
  → print para veririficar o dobor do valor usando a função dobro
  → print para verificar o aumento de valor com 10% usando a função aumento
  → print para verificar o desconto do valor com 10% usando a função diminuir
  → print para verificar a metade do valor usando a função metade'''