import csv

def criar_csv_pessoas():
    # Adicionado o 'r' e a extensão '.csv'
    caminho_arquivo = r"C:\Users\10\Desktop\teste\pessoa.csv" 
    
    pessoas = [
        ["Nome", "Idade", "Cidade"],
        ["Ricardo", 48, "Assis"],
        ["Ric", 48, "Assis"],
        ["Rica", 48, "Assis"],
        ["Cado", 48, "Assis"]
    ]
    try:
        with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(pessoas)
        print(f"Arquivo CSV criado em: {caminho_arquivo}")
    except Exception as erro:
        print(f"Erro detalhado: {erro}") # É melhor imprimir o erro real para debug

criar_csv_pessoas()