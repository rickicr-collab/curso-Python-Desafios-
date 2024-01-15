#função dobro
def dobro(preço = 0):
    resp = preço * 2 
    return resp

#Função metade
def metade(preço = 0):
    resultado = preço / 2
    return resultado     
    

#Função aumentar
def aumentar(preço = 0, taxa = 0):
    resultado =  preço + (preço * taxa / 100)
    return resultado


# função diminuir
def diminuir(preço = 0, taxa = 0):
    resultado = preço - (preço * taxa / 100)
    return resultado
   
    
# função Triplo   
def triplo(num = 0):
    resp = num * 3
    return resp


# função moeda
def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace(".", ",")


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
    junto com valor do preço
    substituindo o caracteres ponto pelo caracatere virgula 
    como padão monetário usado aqui no brasil sem afetar 
    o padrão basico na programação do'''