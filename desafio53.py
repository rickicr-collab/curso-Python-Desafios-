#crie um programa que leia uma frase qualquer e diga se ela é pálindroma , desconsiderando os espaços 
#exemplo  = APOS a SOPA
frase = str(input('Qual é sua frase: ')).strip().upper() # variavel frase criada com funções opçonais .strip / upper 
palavras = frase.split() # função split para separar a frase em strings separados
junto = ''.join(palavras) # função join serve para ignorar os espacos e junta a frase anteriormente separada em strings
inverso = '' # atribui espaço para inverso 
for letra in range(len(junto) - 1, -1, -1): # criando um laço for onde a leitura começa de tras para frente com range final o valor -1 
    inverso += junto[letra] # inverso sendo atribuida com a função junto dentro da variavel do laço for letra
    print('O inverso de {} e {}'.format(junto, inverso)) # imprimindo as funcoes realtivas a variavel junto e inverso
if inverso == junto: # if condicional infrmando que variavel inverso tem que ser igual a variavel junto para se obter uma frase palindroma 
    print('Temos um palindromo!!!') # imprimindo se a frase atribuida se a condição if for atendida 
else:
    print('a frase digitada não é um Palindromo!!!') # imprimindo se a frase atender a condição do else
#--------------------- 02 opção-----------------------#
frase = str(input('Qual é sua frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] # opção de fatiamento disponivel apenas no python fáz a leitura da frase dos termos ao contrario substituindo completamente o laço for
print('O inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!!!')
else:
    print('a frase digitada não é um Palindromo!!!')