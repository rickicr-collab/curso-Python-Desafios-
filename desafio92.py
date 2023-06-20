# crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre -os (com idade)em um dicionario se por acaso a CTPS for diferente de ZERO, o dicionario receberá tambem o ano de contratação e o salario.
# calcule e acrescente, alem da idade. com quantos anos a pessoa vai se aposentar


# --------- Código --------------------#
from datetime import datetime

cadastro = {}
print(f'{" == Cadastro == ":^15}')
cadastro['Nome'] = str(input('Nome:')).capitalize()
nasc = int(input('Data de nascimento:'))
cadastro['Idade'] = nasc- datetime.now().year
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 - não tem carteira de trbalho):'))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de contratação:'))
    cadastro['Salario'] = int(input('Salario(R$):'))
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro["Contratação"] + 32) - datetime.now().year)
    

print('-=-' * 20)
print(f'{"Informações Cadastradas":<10}')
for k, v in cadastro.items():
    print(f' - [{k}] é igual a  → {v}')

print('-=-' * 20)

# -------------- Comentrios do codigo ------------------ #

# importando bliblioteca datetime → modulo datetime

# criado dicionario nome → cadastro
# criado variavel nasc =  para calculo da idade
# criando chaves para dicionario cadastro:
# ['nome']
# ['idade'] = variavel (nasc) - função datetime.now().year
# ['CTPS']

# criado condição if:
    # se cadastro['ctps'] for diferente de 0:
        # criando uma chave cadastro['Contratação] usando função input para ser digitado no teclado
        # criando uma chave cadastro['salario'] usando função input para ser digitado no teclado
        # criando uma chave cadastro['aposentadoria'] que recebe os valores = cadastro['idade] + ((cadastro['contratação] + 32) - datetime.now().year)
        
# criado condição for:
    # para cada k, v em cadstro.items():
        # print formatado informando que os valores de k(keys) recebe os valores de v(values)