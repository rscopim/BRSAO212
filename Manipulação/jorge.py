import csv
import statistics

def analisar_csv(nome_arquivo):
    try:
        # 1. Abrir o arquivo CSV
        with open(nome_arquivo, newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)

            # 2. Extrair valores da coluna "tempo_execucao"
            valores = []
            for linha in leitor:
                try:
                    valores.append(float(linha["tempo_execucao"]))
                except ValueError:
                    # Ignora valores inválidos (não numéricos)
                    pass

        # 3. Calcular média e desvio padrão
        media = statistics.mean(valores)
        desvio = statistics.stdev(valores)

        # 4. Exibir resultados
        print(f"Média da coluna tempo_execucao: {media:.2f}")
        print(f"Desvio padrão da coluna tempo_execucao: {desvio:.2f}")

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro na leitura do arquivo: {e}")

# Exemplo de execução
analisar_csv("dados.csv")