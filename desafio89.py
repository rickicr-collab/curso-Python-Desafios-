# crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usúario possa mostrar as notas de cada aluno individualmente. 


# ------------- comentarios sobre o codigo ----------------- # 

# criado lista 
    # lista criada com nome ficha

# criado laço while:
    # criado variavel nome = para informar o nome dos alunos dentro do laco por ser string recebe classe str com função input
    # criado variavel nota1 = para informar a primeira nota do aluno dentro do laço por ser numero flutuante recebe classe float com função input
    # criado variavel nota2 = para informar a segunda nota do aluno dentro do laço por ser numero flutuante recebe classe float com função input
    # criado variavel media = para calcular a media do aluno apartir das duas primeiras notas dentro do laço é calculado com seguinte formula
        # formaula de calculo da media = (nota1 + nota2) / 2
    # adicionando os dados a lista ficha usando a função append com seguinte estrutura :
        # ficha.append([nome, [nota1, nota2], media])
    # criada variavel resp para perguntar se o usuario deseja adicionar mais elementos dentro do laço por ser string recebe classe primitiva str dentro de um input.
    # criado uma condição para a variavel resposta que quando aceita é interrompido o laço usando a função break

# criado um print com linhas de caraceteres
# criado um print formatado com numeração / nome / e media dos alunos cadastrados para organização e leitura dos dados mais organizados dentro do print
# criado um print com lnnnhas de caracteres

# criado um laço for:
    # criado a condição do laço for indicando o indiçe e alunos usando variavel temporaraia(a) dentro do laço de forma enumerada usando o paramentro (ficha):
        # realizando o print infrmando o indice / nome / media dos alunos de acordo com a formatação do print anterior criadao acima com as respectivas formataçoes de string indicadas no codigo e tambem informando a posiçõa dos dados do indiçe, dos alunos e da media de acordo com posição pre estabelecida dentro da lista ficha.

# criado loop infinito while:
    # criado uma linha de caraceteres para dividir as funções dentro do codigo(para uma organizaçao melhor do codigo)
    # criada variavel opc para inserir os valores inteiros dos indices indicativos dos alunos cadastrados e informado as medias dos mesmo
    # criando uma condição para variavel opc para interromper o laço.
    # criando um print para sinalizar que o laçõ foi interrompido com sucesso 
    # interrompido usando a função break
    # criada uma condição que se o valor digitado em opc for <= ao tamanho existente na lista ficha com diminuição de valor -1
        # criado um frint informando o nome e as notas do aluno apartir de sua posição na lista  ficha 
    # criando um print finalizador do usuario


# ------ Resolução ---------- # 
ficha = []
while True:
    nome = str(input('Digite o nome do Aluno:')).capitalize()
    nota1 = float(input('Digite a Primeira nota:'))
    nota2 = float(input('Digite a Segunda nota:'))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1,nota2], media])
    resp = str(input('Deseja continuar? [S/N]:')).upper()
    if resp == 'N':
        break
print('-=-' * 20)
print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')
print('-=-' * 20)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=-' * 20)
    opc = int(input('Mostrar nota de qual aluno?(000 - interrompe):'))
    if opc == 000:
        print('finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<< Volte Sempre >>>>')