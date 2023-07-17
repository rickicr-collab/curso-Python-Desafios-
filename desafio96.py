''' Faça um programa que tenha uma função 
chamada area().que receba as dimensões de 
um terreno retangular (largura e comprimento)
e mostre area do terreno'''

# função para apresentalão em titulo
def apresentação(txt):
    print('----------------------')
    print(txt)
    print('----------------------')

    
# função para calculo da area 
def area(largura, comprimento):
    resultado = (largura * comprimento)
    print(f'A area de um terreno {largura} x {comprimento} é de {resultado:.1f} m²')
    

# programa principal  
apresentação(' Controle de Terreno ')
largura = float(input('Largura(m):'))
comprimento = float(input('Comprimento(m):'))
print('-----------------------------')
area(largura, comprimento) 


# ======== Comentario do Codigo ========== #

# funções Criadas:
    # apresentação
''' Criado uma função apresentação para estilizar o inicio do programa 
a ser criado '''

# função area:
'''criada função area com parametros sendo eles:
largura = recebe o valor representando largura
comprimento = recebe o valor representando comprimento'''
'''a variavel resultado foi criada para verificar o resultado com calculo sendo 
resultado = (largura * comprimento)
mostrando um print informando os resultados do calculo acima:
→ print(f'A area de um terreno {largura} x {comprimento} é de {resultado:.1f}m²') 
 realizano uma pequena formatação nos valores flutuantes resultantes da operação limitando a um valor '''
 
# programa principal

''' Função apresentação recebe o parametro → (' Controle de terreno ')'''
''' variavel largura que recebe valor por input → largura = float(input('Largura(m):))'''
''' variavel comprimento que recebe valor por input → comprimento = float(input('comprimento(m):))'''
''' print com caracteres divisorios (opçional)'''
''' função area com paramentros → (largura, Comprimento)'''