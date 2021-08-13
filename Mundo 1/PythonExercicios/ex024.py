print('===== Exercicio 024 =====')
print('Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO"')

cidade = input('Digite o nome de uma cidade: ')

cidadeFormated = cidade.lower().split()

if cidadeFormated[0] == 'santo':
    print('Começa!')
else:
    print('Não começa!')
