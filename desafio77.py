#crie um programa que tenha uma tupla com varias palavras (não usar acentos).Depois disso você deve mostrar , para cada palavra quais são as suas vogais.

palavras = ('Espada','Tribulacao','Ascencao',
            'Imortal','Celestial','Alquimia',
            'Ferraria','Caminho','Superacao',
            'Primordial','Companheiro','coracao')

# criando um laço for para que para cada palavra dentro da tupla seja impreso as informacoes infomradas no print
# para cada letra dentro da variavel temporaria (p) no naço for informado quantas vogais em string está dentro de cada palavra na tupla
# criando uma condição if com função lower para que as letras dentro da tupla palavra em minusculo sejá indentificada e informada na tela atraves do print
# criando um print para imprimir as vogais indentificas nas palavras dentro da tupla contendo as vogasi 'aeiou'
for p in palavras:
    print(f'\nNas palavras {p.capitalize()} temos → ', end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
