'''1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente.'''

import random
import string
def gerar_senha(tamanho: int) -> str:
    caractere = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(caractere) for _ in range(tamanho))
tamanho_senha = int(input("Digite o tamanho da senha: "))
senha = gerar_senha(tamanho_senha)
print(f"Senha gerada: {senha}")