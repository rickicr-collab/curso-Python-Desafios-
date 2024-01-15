#função dobro
def dobro(preço = 0, formato = False):
    resp = preço * 2 
    return resp if not formato else moeda(resp)

#Função metade
def metade(preço = 0, formato = False):
    resultado = preço / 2
    return resultado if not formato else moeda(resultado)    
    

#Função aumentar
def aumentar(preço, taxa, formato = False):
    resultado =  preço + (preço * taxa / 100)
    return resultado if formato is False else moeda(resultado)


# função diminuir
def diminuir(preço, taxa, formato = False):
    resultado = preço - (preço * taxa / 100)
    return resultado if formato is False else moeda(resultado)
   
    
# função Triplo   
def triplo(num, formato = False):
    resp = num * 3
    return resp if not formato else moeda(resp)


# função moeda
def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço = 0, taxaa = 10, taxar = 5):
    print('-' * 30)
    print('Função Resumo'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(preço)}')
    print(f'O dobro do preço é:\t{dobro(preço, True)}')
    print(f'O triplo do preço é:\t{triplo(preço, True)}')
    print(f'A metade do preço é:\t{metade(preço, True)}')
    print(f'Com {taxaa}% de aumento:\t{aumentar(preço, taxaa,  True)}')
    print(f'Com {taxar}% de redução:\t{diminuir(preço, taxar,  True)}')
    print('-' * 30)

# ===== Comentarios do codiogo ===== #

# funçoes criadas

# Função dobro
'''Criada funnção dobro com paramentro : preço
    criada variavel resp que recebe = preço * 2
    retornar o valor da variavel resp'''
    
#função metade
''' criada função metade com parametro: preço
    criada variavel resp que recebe = preço / 2
    retornar o valor da variavel resp '''
    
# função aumentar
''' criada função aumentar com parametros: preço, taxa
    criada variavel resultado que receb = preço + (preço * taxa / 100)
    retornar o valor da variavel resultado '''
    
# função diminuir
''' criada função diminuir com paramentros: preço, taxa
    criada variavel resultado que recebe = preço - (preço * taxa / 100)
    retornar o valor da variavel resultado '''
    
# função Triplo
''' criada função triplo com parametros: num
    criada variavel resp que recebe = num * 3
    retorna o valor da variavel resp'''
    
# função moeda
''' criada função moeda com parametro: preço
    retornado o valor formadado com caracteres monetarios 
    junto com valor do preço'''
    
# observação:
''' para que as funções sejam executadas sem perder as formataçoes 
    feitas anteriormente foram aplicadas as seguintes alterações nas funçoes:
    criado um parametro chamado formato que vem por padrão false
    e na mesma linha do return criado uma condição if para que se o format não for 
    chamado é aplicado a função moeda da variavel da função local ativa '''
    
# função Resumo
''' 
  → criada função resumo que contem os seguintes paramentros:
    preço, taxaa(taxa de aumento), taxar(taxa de redução)
  → criado um print estilizado com linhas divisorias supeirores e 
    inferiores contendo 30 caracteres
    crido um titulo formatado usando a função center(30)
    para que o texto fosse centralizado a 30 caracteres
    prints formatados com as seguintes funções:
  → print formatado da função moeda = moeda(preço) 
  → print formatado da funçãp dobro = dobro(preço, True)
  → print formatado da função metade = metade(preço, True)
  → print formatado da função aumentar com parametro taxaa informado com valor previo = 0 = f'{taxaa}' {aumentar(preço, taxaa, True)}
  → print formatado da função diminuir com parametro taxar informado com valor previo = 0 = f'{taxar}' {diminuir(preço, taxar, True)} 
  OBs: usado o caractere \t para realizar tabulação para alinhar os dados tabulados
  pode se usar quantas tabulaçoes forem necessarias no codigo para organizalo'''