#crie um programa que leio sexo de uma pessoa mas so aceita os valores M 0u F caso esteja errado peça a digitação novamente até ter um valor correto
s = 0
while s != 'M' and s != 'F': # para mais de um caractere na condição favoravel usar a opção and inves do or
  print('''Selecione uma das opções abaixo:
[ M ] - Masculino
[ F ] - Feminino ''')
  s= str(input('Qual o Sexo [M/F]:')).strip().upper()#criando uma string com input para especificar a resposta no teclado com função strip e função upper
  if s != 'M' and s != 'F': # condição if para que quqlquer caractere diferente da condição ele imprimir uma imagem na tela 
    print('Dados invalidos tente novamente')
print('Sexo {} Registrado com sucesso'.format(s)) # print informando que a resposta do input foi registrada com sucesso 
print('Fim do Programa!!')

# ----------  02 opção -------------
sexo = str(input('Informe seu sexo : ')).strip().upper()[0] # criado a variavel sexo com alterações de string opcionais como strip / upper
while sexo not in 'MmFf': # condição while sobre caracteres strings 'MmFf'  quando esses caracteres não foram inseridos antecipadamente na variavel sexo anterior
  sexo = str(input('Dados Invalidos. por favor, informe seu sexo: ')).strip().upper()[0] 
print('Sexo {} registrado com sucesso.'.format(sexo))