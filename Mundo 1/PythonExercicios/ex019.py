import random

print('===== EXERCICIO 019 =====')
print('- Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido -')

alunoa = input('Qual o nome do primeiro aluno? ')
alunob = input('Qual o nome do segundo aluno? ')
alunoc = input('Qual o nome do terceiro aluno? ')
alunod = input('Qual o nome do quarto aluno? ')

alunos = [alunoa, alunob, alunoc, alunod]
print(random.choice(alunos))
