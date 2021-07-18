from random import shuffle

print('===== EXERCICIO 020 =====')
print('- O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada -')


alunoa = input('Qual o nome do primeiro aluno? ')
alunob = input('Qual o nome do segundo aluno? ')
alunoc = input('Qual o nome do terceiro aluno? ')
alunod = input('Qual o nome do quarto aluno? ')

alunos = [alunoa, alunob, alunoc, alunod]
shuffle(alunos)

i = 0
for item in alunos:
    i += 1
    print('{}-{}'.format(i, item))

