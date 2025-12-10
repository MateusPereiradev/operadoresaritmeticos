from random import sample
alunos= str(input('Digite aqui os alunos participantes separados por vírgula:')).strip().upper().split(',')
print(f'A ordem para apresentação do trabalho será: {sample(alunos, 4)}')


'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.

'''

