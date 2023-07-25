'''
   Faça um programa que tenha uma 
   função chamada notas() que pode receber 
   varias notas de alunos e vai retornar
   um dicionario com as seguintes informaçoes:
   - Quantidade de notas
   - A maior nota
   - A menor nota
   - A média da turma
   - A situação (opçional)
   adicone tambem os docstrings da função
'''

def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)


def notas(* num, situação = False):
    """_summary_
    -> Criado um dicionario que adicionar notas em chaves e exibe em tela
    Args:
    num: varios valores numericos representando as notas
    situação: argumento opcional mostrando a situação de acordo com as medias / por padrão falso
    Returns:
    r _type_: retornando os valores declarados no dicionario em tela 
    """
    r = dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num) / len(num)
    if situação:
        if r['media'] >= 7:
            r['situação'] = 'Situação Otima'
        elif r['media'] >= 5:
            r['situação'] = 'Situação razoavel'
        else:
            r['media'] = 'Situação Ruim'
    return r


#programa principal 
titulo(f' {" Função Notas "}')
resp = notas(5.5, 6.5, 9, 6.8, situação = True)
print(resp)
print('-' * 50)
help(notas)
print('-' * 50)



# ====== Comentarios do Codigo ========== # 

# funções Criadas 

# função titulo
''' Criada para estilizar o codigo com um titulo inicial com
    caracteres divisorios no titulo '''
    
# função notas()
''' criada a função notas com argumentos: ( * num, Situação = False( valor opcional))
    criado docstring informando sobre argumentos , retorno e o sumario que seria o resumo da função.
    criado dicionario r → r = dict()
    criada chave total no dicionário r → r['total'] = len(num) total de valores adicionario no dicionario
    criada chave maior no dicionário r → r['maior'] = max(num) maior valor adicionado no dicionário
    criada chave menor no dicionário r → r['menor'] = max(num) menor valor adicionado no dicionário
    criada chave media no dicionário r → r['media'] = sum(num) / len(num) a soma dos valores dividio pelo total de notas adicionas no dicionário
    criada condição if para situação → if situação:
        se media for maior ou igual a 7:
            cria uma chave r['situação'] = 'Situação Boa' → referente a media superio ou igual a 7
        se então media for maior ou igual a 5:
            cria uma chave r['situação'] = 'Situação Razoavel' → referente a media ser superior ou igual a 5
        se não atender a nenhumas das condição anteriores:
            cria uma chave r['situação'] = 'Situação Ruim' → referente a media ser inferior a 5
    retornando o valor declarado de r'''
    
# programa principal
''' função titulo que rebebe o parametro informado : função notas'''
''' variavel resp recebe função notas com parametros numeros e situação como verdadeiro
  → resp = notas(varias notas informadas , situação = valor booleano True)'''
''' print mostrando as informaçoes solicitadas da variavel resp que recebe função notas → print(resp)'''
''' criada linhas de caracteres divisorios 
    chamada função help do paramentro sobre função notas para verificar informaçoes uteis sobre a mesma
    criada novamente linha de caracteres divisores'''

