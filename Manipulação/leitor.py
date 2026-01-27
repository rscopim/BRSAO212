'''3 -  Crie um programa que leia um arquivo CSV informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado, mostre uma mensagem de erro.'''

import csv
import os
def ler_csv():
    caminho_arquivo = input("Informe o caminho do arquivo: ")
    try:
        if not os.path.exists(caminho_arquivo):
            raise FileNotFoundError("Arquivo não encontrado.")
        with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            print("\nConteúdo do arquivo: ")
            for linha in leitor:
                print(linha)
    except Exception as erro:
        print(f"Erro ao ler: {erro}")
ler_csv()