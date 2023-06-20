# faça um programa que leia nome e média de um aluno guardando tambem a situação em um dicionario.
# no final mostre o conteudo da estrutura na tela 
# se o valor da media for igual ou superior a 7 aprovado 
# se for inferior a 7 reprovado

# -------- código do desafio ---------------#
boletim = {}

boletim['Nome'] = str(input('Digite o nome do aluno:')).capitalize()
boletim['Media'] = float(input(f'Digite a media de {boletim["Nome"]}:'))


print('-=-' * 20)
if boletim["Media"] >= 7:
    boletim["Situação"] = 'Aprovado'
elif 5 <= boletim['Media'] < 7:
    boletim["Situação"] = 'Recuperação'
else:
    boletim["Situação"] = 'Reprovado'
    
for k, v in boletim.items():
    print(f' - {k} é igual a {v}')

print('-=-' * 20)

# --------- comentarios sobre o codigo ----------------#


# Criado um dicionario chamado boletim

# criado duas chaves 
    # criado chave chamado nome que recebe um input com valores em string com função capitalize para deixar primeira letra do nome em maiusculo
    # criado chave chamado média que recebe um input com valores em float informando valores flutuantes para media do aluno


# criada condição if para situação de Media :
    # onde se o valor em Media fosse maior que 7
        # então o aluno seria aprovado
    # se o valor entivisse entre 5 e 7 
        # então o aluno estaria em recuperação
    # se as condição anteriores não forem atendidas
        # então o aluno estaria reprovado
        
# crido um laço for:
    # onde keys e values no dicionario boletim usando função items()
        # realizar o print formatado onde mostrava as chaves era igual as suas informações 