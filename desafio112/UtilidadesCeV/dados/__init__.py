
# função leiadinheiro
def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
           print(f'\033[31mERRO!\"{entrada}\" não é preço válido.\033[m')
        else:
            valido = True
            return float(entrada)
    

# função leiaint
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! - Digite apenas valores Numéricos validos.\033[m')
        if ok:
            break
    return valor
    
    

# ==== Comentarios do Código ==== #

# função leiaint
'''criada função leiaint com paramentros: num recebendo valor opcional 0'''
'''criada condição if → if leiaint:
   criada variavel num que recebe os seguintes valores:
 → num = input('Digite um numero:) 
   criada outra condição if → if num.isnumeric():
 → num = int(num) 
   print(f'O numero digitado é {num}')
   com formatação de de cor no texto
   else:
 → realiza um print informando que o valor foi digitado erroneamente
 → com codigos de formatação de cores no texto')'''
 

# função Leiadinheiro
''' crida função leiadinheiro com parametro: (msg)
    criada variavel valido que recebe valor inicial = False
  → criado laco while = while not valido:
    variavel entrada recebendo um input com valores a serem informados como string
    recebendo um replace para substituir os pontos por virgula sem modificar função
    interna do python com função de retirador de espaços desnecessarios strip().
  → criado condição if = if entrada.isalpha() or entrada == '':
    realizo um print informando sobre os erros das condições if informadas acima
    com formatação com a frase na cor vermelha.
  → criado condição else se o if anterior não for antendido:
    variavel valido recebe o valor = True
    retornando o valor float(flutuante ou real) da variavel entrada
'''