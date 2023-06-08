#desenvolva um prgrama que leia o primeiro termo e a razão de uma PA.no final mostre os 10 primeiros termos dessa regressão
#calculando uma PA 
import emoji

print('-=-' * 10)
print(' Calculando PA ')
print('-=-' * 10)
primeiro = int(input('Primeiro termo:')) # criando variavel primeiro referente ao primeiro termo de uma PA( progressão aritmetica)
razão = int(input('Digite a razão:')) # criando a variavel razão de uma PA ( progressão aritmetica)
décimo = primeiro + (10 - 1) * razão # criando a variavel com formula para indentificar o ultimo termo para a progressão aritmetica que no caso proposto seria o 10
for c in range(primeiro, décimo + razão, razão): # criado um lanço for com intervalo substituido pelas variaveis declaradas anteriormente somando as variaveis decimo + razão 
        print('{}'.format(c), end=' \u27A1\uFE0F  ') # realizando um print da variavel declarada c usando opção de emoji para separar os valores da progressão aritmetica 
print('ACABOU !!') # criando um print para apenas mostrar o final da operação da Progressão aritmetica