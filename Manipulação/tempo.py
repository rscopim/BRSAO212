import csv
import re

# Função para converter uma string de tempo (anos, meses, dias) em um total estimado de dias
def converter_para_dias(tempo_str):
    """Converte a string de tempo (anos, meses, dias) para um total estimado de dias."""
    # Padrão: "X anos, Y meses e Z dias"
    match = re.search(r"(\d+) anos, (\d+) meses e (\d+) dias", tempo_str)
    if match:
        anos, meses, dias = map(int, match.groups())
        # Estimativa: 1 ano = 365 dias, 1 mês = 30 dias
        return (anos * 365) + (meses * 30) + dias
    return None

def analisar_tempo_execucao():
    """
    Lê um arquivo CSV e calcula a média e o máximo da coluna 'tempo_execucao'.
    """
    # Solicita ao usuário o caminho do arquivo CSV
    arquivo = input("Digite o caminho do arquivo CSV: ")
    
    # Lista para armazenar os tempos convertidos
    tempos = []
    
    try:
        # Abre o arquivo CSV para leitura
        with open(arquivo, mode='r', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            
            # Itera sobre cada linha do CSV
            for linha in leitor:
                # Verifica se a coluna 'tempo_execucao' existe e tem valor
                if 'tempo_execucao' in linha and linha['tempo_execucao']:
                    texto_tempo = linha['tempo_execucao']
                    try:
                        # Tenta converter diretamente para float (caso seja numérico)
                        valor = float(texto_tempo)
                        tempos.append(valor)
                    except ValueError:
                        # Se não for numérico, tenta converter usando a função auxiliar
                        dias = converter_para_dias(texto_tempo)
                        if dias is not None:
                            tempos.append(dias)
        
        # Se houver tempos válidos, calcula média e máximo
        if tempos:
            media = sum(tempos) / len(tempos)
            maximo = max(tempos)
            print(f"\nAnálise da coluna 'tempo_execucao' (em dias estimados):")
            print(f"Média: {media:.2f} dias")
            print(f"Máximo: {maximo:.2f} dias")
        else:
            print("Não foram encontrados dados válidos na coluna 'tempo_execucao'.")
            
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    # Executa a função principal se o script for rodado diretamente
    analisar_tempo_execucao()