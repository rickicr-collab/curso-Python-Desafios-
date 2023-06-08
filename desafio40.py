#crie um programa que leia duas notas de um aluno e calcule sua media mostrando uma mensagem no final de acordo com a media atingida 
#media abaixo de 5.0: reprovado 
#media entre 5.0 e 6.9 recuperação
#media 7.0 ou superior: aprovado 
print('-=-'*20)
nota01 = float(input('Digite a primeira nota:'))
nota02 = float(input('Digite a segunda nota:'))
print('-=-'*20)
media = (nota01 + nota02) / 2
if media < 5.0:
    print(' Você ficou com média, {} e foi REPROVADO estude mais!'.format(media))
elif media == 5.0 or media <= 6.9:
    print('Voce ficou com média, {} e está em RECUPERAÇÂO estude mais !'.format(media))
elif media >= 7.0:
    print('Você ficou com média, {} e está APROVADO parabens'.format(media))