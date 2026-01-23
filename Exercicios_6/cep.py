'''3 - Crie um programa que consulte informações de um CEP na API ViaCEP, retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.

url = f"https://viacep.com.br/ws/{cep}/json/"
'''

import requests
def consulta_cep(cep: str) -> dict:
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()
    return resposta.json()
try:
    cep_usuario = input("Digite o seu CEP: ")
    dados = consulta_cep(cep_usuario)
    if dados.get("Erro"):
        raise ValueError("CEP não encontrado")
    print(f"Logradouro: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
    print(f"Estado: {dados['uf']}")
except Exception:
    print("Erro ao consultar o CEP.")
    