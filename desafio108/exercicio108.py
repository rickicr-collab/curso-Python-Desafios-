''' Adapte o codigo do desafio 107
    , criando uma função adiconal
    chamada moeda() que consiga mostrar
    os valores como um valor monetário
    formatado
'''
# importação do modulo 
from utilitarios import aumentar
from utilitarios import diminuir
from utilitarios import metade
from utilitarios import dobro
from utilitarios import moeda

# função 
def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    

# programa principal   
titulo(f' {" Modulos Teste "}')
valor = float(input('Digite o valor (R$):'))
print(f'O dobro do {moeda(valor)} digitado fica: {moeda(dobro(valor))}')
print(f'O valor de {moeda(valor)} com 10% de aumento fica: {moeda(aumentar(valor, 10))}')
print(f'O valor de {moeda(valor)} com 10% de desconto fica: {moeda(diminuir(valor, 10))}')
print(f'A metade de {moeda(valor)} fica: {moeda(metade(valor))}')


# ===== Comentarios do Código ===== #

# modulos
''' Modulo moeda importado função moeda'''

# função Titulo
''' Função titulo criada para gerar um titulo inicial
    que estiliza a inicialização do programa'''

# Programa principal
''' Titulo com paramentro contento texto definido pelo usuario'''

''' variavel valor que recebe um unput contendo classe primitiva pré 
    definida como classe flooat → flutuantes ou numeros reais '''

''' print formatado contendo texto pré-definido contendo a função moeda
    para organizar os valores de forma monetária 
    no print formatado incluindo a função moeda para variavel valor 
    em cada print pra mostrar os valores na variavel formatado 
    para o padão monétario brasileiro '''

''' as funçoes dobro , aumentar, diminuir e metade para possuir
    os valores formatados com padrão monetário brasileiro 
    precisa ser passados como parametro dentro da função moeda 
    sem alterar seus valores internos'''