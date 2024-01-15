'''Crie um pacote chamado utilidadeCev
   que tenha dos modulos internos chamados 
   moedas e dados.
     
   transfira todas as funçoes utilizadas 
   nos desafios 107 a 109 para o primeiro 
   pacote e mantenha tudo funcionando.
'''

# pacotes importados 
from UtilidadesCeV import moeda


# programa Principal
valor = int(input('Digite um valor:'))
moeda.resumo(valor, 10, 5)


# ==== Comentarios do Código ==== #

''' Pacote UtilidadesCEV Criado e do mesmo importado a função resumo
   do modulo moeda.'''

''' variavel valor criada que recebe um input para dados de valor inteiro '''

'''Função resumo chamada com paramentros:
 → valor (variavel pré criada)
 → taxa de aumento da função resumo: valor 20
 → taxa de redução da função resumo: valor 5 '''