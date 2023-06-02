# crie um programa onde o usuario digite uam expresão qualquer que use parenteses . seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta


# ----------------------------------------------------------------------------------

#criando a variavel expressão como input para digitar valor pelo teclado
expressão = str(input('Digite uma expressão: '))
# criado uma lista com nome pilha vazia
pilha = []

for simb in expressão:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop() 
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('sua expressão está invalida!!!')
