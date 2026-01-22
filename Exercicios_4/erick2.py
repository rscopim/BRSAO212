alunos = []

print("--- Sistema de Registro de Notas ---")
print("Digite 'sair' no nome do aluno para finalizar e ver o resultado.\n")

while True:
    nome = input("Digite o nome do aluno: ")
    
    if nome.lower() == 'sair':
        break
    
    try:
        nota = float(input(f"Digite a nota de {nome}: "))
        alunos.append({"nome": nome, "nota": nota})
    except ValueError:
        print("Erro: Por favor, insira um número válido para a nota.")

if len(alunos) > 0:
    soma_notas = 0
    
    print("\n--- Relatório Final ---")
    for aluno in alunos:
        print(f"Aluno: {aluno['nome']} | Nota: {aluno['nota']:.2f}")
        soma_notas += aluno['nota']
    
    media_turma = soma_notas / len(alunos)
    
    print("--------------------------------")
    print(f"Total de alunos: {len(alunos)}")
    print(f"Média Geral da Turma: {media_turma:.2f}")
else:
    print("\nNenhum aluno foi registrado.")