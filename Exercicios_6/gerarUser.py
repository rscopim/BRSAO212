'''2 -   Crie um programa que  acesse a API Random User Generator para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.
url = "https://randomuser.me/api/"'''

import requests
def criar_usuarios() -> dict:
    url = "https://randomuser.me/api/"
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()
    return resposta.json()
try:
    dados = criar_usuarios()
    usuario = dados["results"][0]
    nome = f"{usuario["name"]["first"]} {usuario["name"]["last"]}"
    email = usuario["email"]
    pais = usuario["location"]["country"]
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"Pais: {pais}")
except Exception:
    print("Usuário não encontrado.")