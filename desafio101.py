''' Crie um programa que 
tenha uma função chamada voto() que 
vai receber como parametro o ano de nascimento
de uma pessoa, retornando um valor literal
indicando se uma pessoa tem voto negado, opçional
ou obrigatorio nas eleiçoes'''


# função titulo
def titulo(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f' {msg}')
    print('-' * tam)
    
 
 # função voto    
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: \033[32mNão necessita Voto\033[m'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos. \033[33mVoto não é Obrigatório\033[m'
    else:
        return f'Com {idade} anos: \033[31mVoto é Obrigatório\033[m'
    
    
# programa Principal 
titulo(f' {" Verificador de Voto Eleitoral "}')
ano = int(input('Digite o ano de nascimento:'))
print(voto(ano))


# ===========  Comentários do Código ============ #

# Funções Criadas:

# titulo
''' Função titulo criada para estilizar um titulo inicial para
o programa criado '''

# função voto:

''' criada função voto com parametros sendo ele : (ano)
importado bliblioteca datetime importando date → from datetime import date
variavel criadas:
atual = date.today().year
idade = atual - ano (parametro associadoa função voto)
'''

# criado condição if:
    # se a idade for menor que 16: → if idade < 16:
''' realiza um return → com {idade} anos: \033[32m Não necessica Voto \033[m
    Utilizando paramentros de cores na mensagem'''
    # se a idade for entre 16 e menos de 18 ou acima de 65 anos → if 16 <= idade < 18 or idade > 65:
''' realiza um return → com {idade} anos: \033[33m Voto não sendo Obrigatório \033[m
    utilizando paramentros de cores na mensagem'''
    # condição else:
''' realiza um return → com {idade} anos: \033[31m Voto é Obrigatório \033[m
    utilizando paramentros de cores na mensagem'''
    
# programa Principal 

''' Função titulo que recebe → (f' {" Verificador de Voto Eleitoral "}')'''
''' variavel ano que recebe → ano = int (input('Digite o ano de nascimento:))'''
''' função print que recebe → print(voto(ano))'''