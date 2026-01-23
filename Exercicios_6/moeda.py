'''4 - Crie um programa que realize consultas a cotações de moedas em relação ao Real (BRL) usando a API AwesomeAPI, mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.

url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
'''
import requests
from datetime import datetime
def consulta_moeda(moeda: str) -> dict:
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()
    return resposta.json()
try:
    moeda = input("Digite a moeda (USD, EUR): ").upper()
    dados = consulta_moeda(moeda)
    chave = f"{moeda}BRL"
    cotacao = dados[chave]
    data_hora = datetime.fromtimestamp(int(cotacao["timestamp"]))
    print(f"Moeda: {moeda}/BRL")
    print(f"Valor atual: R$ {float(cotacao["bid"]):.2f}")
    print(f"Valor máximo: R$ {float(cotacao["high"]):.2f}")
    print(f"Valor mínimo: R$ {float(cotacao["low"]):.2f}")
    print(f"Data da atualização: {data_hora.strftime("%D %H:%m:%S")}")
except Exception:
    print("Erro ao consultar moeda.")