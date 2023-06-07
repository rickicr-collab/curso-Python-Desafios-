#crie um programa que leia o nome de uma pessoa e diga se ela tem o nome 'SILVA' no nome. 
nome = str(input('Digite seu nome:')).strip().capitalize() # criado variavel nome com classe primitiva string / aplicando função strip para eliminar espacos esquerdos e direitos desnecessarios
print('Seu nome tem silva:{}'.format('silva' in nome)) # imprimindo informaçoes da variavel nome com função In nome.capitalize() para realizar a formatação no nome ao ser inserido com função capitalize 
