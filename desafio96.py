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