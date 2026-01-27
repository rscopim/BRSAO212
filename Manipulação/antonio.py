import csv
import random

def criar_arquivo_pessoas():
    """
    Cria um arquivo CSV com dados de pessoas gerados dinamicamente.
    """
    try:
        qtd_linhas = int(input("Quantas linhas de dados deseja gerar? "))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        return

    # Dados a serem escritos
    cabecalho = ["Nome", "Idade", "Cidade", "Profissão", "Salário", "tempo_execucao"]
    
    nomes_base = ["Ana", "Bruno", "Carla", "Daniel", "Elisa", "Fernando", "Gabriela", "Hugo"]
    sobrenomes_base = ["Silva", "Souza", "Dias", "Rocha", "Martins", "Ferreira", "Almeida", "Costa"]
    cidades_base = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Salvador", "Brasília"]
    profissoes_base = ["Engenheiro", "Analista", "Gerente", "Desenvolvedor", "Designer", "Consultor"]

    dados = []
    for _ in range(qtd_linhas):
        nome = f"{random.choice(nomes_base)} {random.choice(sobrenomes_base)}"
        idade = random.randint(18, 70)
        cidade = random.choice(cidades_base)
        profissao = random.choice(profissoes_base)
        salario = round(random.uniform(3000, 15000), 2)
        anos = random.randint(0, 10)
        meses = random.randint(0, 11)
        dias = random.randint(0, 30)
        tempo_execucao = f"{anos} anos, {meses} meses e {dias} dias"
        
        dados.append([nome, idade, cidade, profissao, salario, tempo_execucao])
    
    nome_arquivo = input("Digite o nome do arquivo para salvar (ex: pessoas.csv): ")
    
    try:
        # newline='' é importante para evitar linhas em branco extras no Windows
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(cabecalho)
            escritor.writerows(dados)
            
        print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
        
    except Exception as e:
        print(f"Falha ao salvar o arquivo: {e}")

if __name__ == "__main__":
    criar_arquivo_pessoas()