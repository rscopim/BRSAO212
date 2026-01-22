'''2 - Criar um código que registre as notas de alunos e calcular a média da turma.
'''
notas = []
quantidade_alunos = int(input("Digite a quantidade de alunos: "))
for i in range(quantidade_alunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)
media = sum(notas) / quantidade_alunos
print("Notas dos alunos: ", notas)
print("Média dos alunos: ", round(media, 2))