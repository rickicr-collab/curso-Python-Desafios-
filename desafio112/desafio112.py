''' Dentro do pacote utilidadesCev que criamos
    no desafio 111, temos um modulo chamado
    dado.Cria uma função chamada leiaDinheiro()
    que seja capaz de funcionar como a função input()
    mais com uma validação de dados para aceitar 
    apenas valores que sejam monetários
'''
# pacotes e modulos importados 
from UtilidadesCeV import dados
from UtilidadesCeV import moeda



# programa Principal 
valor = dados.leiadinheiro('Digite um preço R$:')
moeda.resumo(valor, 20, 12)


# ==== Comentarios do Codigo ==== #

# pacotes e modulos importados 
''' importado do pacote UtilidadesCEV os modulos : dados , moeda'''

#programa principal 

''' criado variavel p que recebe função → dados.leiadinheiro
    do modulo dados
    chamada a função resumo do modulo moeda para os seguintes paramentros:
    valor = varivael contendo função leiadinheiro
    20 = taxa de aumento da função resumo
    12 = taxa de redução da função resumo'''