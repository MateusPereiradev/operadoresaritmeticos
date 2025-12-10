from random import sample
aluno= str(input("Digite aqui o nome dos alunos separados por vírgula:")).strip().split()
print(f"A ordem de apresentação do trabalho, será {sample(aluno, 4)}")

'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.

'''

