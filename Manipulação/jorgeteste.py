def main():
    # Passo 1: Solicitar ao usuário o nome do arquivo
    nome_arquivo = input("Digite o nome do arquivo: ")

    try:
        # Passo 2: Abrir o arquivo no modo leitura
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            # Passo 3: Percorrer cada linha do arquivo
            for linha in arquivo:
                # Passo 4: Exibir a linha na tela (removendo quebras extras)
                print(linha.strip())
    
    except FileNotFoundError:
        # Passo 5: Caso o arquivo não seja encontrado, mostrar mensagem de erro
        print("Erro: Arquivo não encontrado.")

if __name__ == "__main__":
    main()