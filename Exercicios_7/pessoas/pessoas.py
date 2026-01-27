'''2 - Crie um programa que cria um arquivo CSV com nome, idade e cidade de algumas pessoas, que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha. '''

import csv
def criar_csv_pessoas():
    caminho_arquivo = "C:\Users\10\Desktop\TurmasEDN\BRSAO212\BRSAO212\Exercicios_7\pessoas.csv"
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
        print(f"Falha ao salvar CSV: {caminho_arquivo}")
criar_csv_pessoas()