''' Modifique os funções que forem
    criadas no desafio 107 para que
    elas aceitem um parametro a mais
    ,informando se o valor retornado
    por elas vai ser ou não formatado
    pela função moeda(), desenvolvida
    no desafio 108
'''

import utilitarios


valor = float(input('Digite um valor(R$):'))
print(f'O dobro do valor de {utilitarios.moeda(valor)} é: {utilitarios.dobro(valor, True)}')
print(f'O valor aumentado de {utilitarios.moeda(valor)} em 10% fica: {utilitarios.aumentar(valor, 10, True)}')
print(f'O valor reduzido de {utilitarios.moeda(valor)} em 10% fica: {utilitarios.diminuir(valor, 10, True)}')
print(f'A metade de {utilitarios.moeda(valor)} fica: {utilitarios.metade(valor, True)}')


# ===== Comentarios sobre o Codigo =====# 

''' feitas as alterações no codigos das funçoes no arquivo utilitarios 
    e criado farametro novo chamado formato que vem por padrão False
    foi aplicado que caso o mesmo parametro formato receba o valor True
    cada função alterada irá receber a alteração realizada na função moeda()
    para modificar os caracteres '.' por caractere ',' como simbolo de valor
    monetário padrão brasileiro'''