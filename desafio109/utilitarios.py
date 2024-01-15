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