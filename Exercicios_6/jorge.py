import requests

def consultar_moeda(moeda):
    try:
        # URL da API (AwesomeAPI) para consultar em relação ao Real (BRL)
        url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
        resposta = requests.get(url)

        # Verifica se a requisição foi bem-sucedida
        if resposta.status_code != 200:
            return f"Erro na requisição: código {resposta.status_code}"

        dados = resposta.json()

        # A chave no JSON é formada pelo par de moedas, ex: "USDBRL"
        chave = f"{moeda}BRL"
        if chave not in dados:
            return "Moeda não encontrada ou inválida."

        info = dados[chave]

        # Extrai os valores necessários
        valor_atual = info["bid"]
        valor_maximo = info["high"]
        valor_minimo = info["low"]
        ultima_atualizacao = info["create_date"]

        # Retorna os dados formatados
        return (
            f"Moeda: {moeda}/BRL\n"
            f"Valor atual: R$ {valor_atual}\n"
            f"Máximo: R$ {valor_maximo}\n"
            f"Mínimo: R$ {valor_minimo}\n"
            f"Última atualização: {ultima_atualizacao}"
        )

    except Exception as e:
        return f"Ocorreu um erro: {e}"

# Exemplo de uso
print(consultar_moeda("USD"))  # Consulta Dólar em relação ao Real
print(consultar_moeda("EUR"))  # Consulta Euro em relação ao Real
print(consultar_moeda("ABC"))  # Teste com moeda inexistente