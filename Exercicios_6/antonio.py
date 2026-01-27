import random
import string

def gerar_senha(tamanho):
    # Define os caracteres possíveis: letras maiúsculas, minúsculas, números e símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Gera a senha aleatória
    senha = ''.join(random.choices(caracteres, k=tamanho))
    return senha

def main():
    print("Gerador de Senhas Seguras")
    print("=========================")

    while True:
        try:
            # Solicita o tamanho da senha ao usuário
            tamanho = int(input("Digite o tamanho da senha (mínimo 8 para segurança): "))
            if tamanho < 8:
                print("Para uma senha segura, recomendamos pelo menos 8 caracteres.")
                continue
            elif tamanho <= 0:
                print("O tamanho deve ser um número positivo.")
                continue

            # Gera e exibe a senha
            senha = gerar_senha(tamanho)
            print(f"Senha gerada: {senha}")

            # Pergunta se o usuário quer gerar outra senha
            continuar = input("Deseja gerar outra senha? (s/n): ").lower()
            if continuar != 's':
                break

        except ValueError:
            print("Por favor, digite um número válido para o tamanho.")

    print("Obrigado por usar o gerador de senhas!")

if __name__ == "__main__":
    main()