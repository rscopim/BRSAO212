'''3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.'''

def calcular_desconto(preco: float, percentual: float) -> float:
    desconto = preco * (percentual / 100)
    return preco - desconto
nome_produto = input("Digite o nome do produto: ")
preco_original = float(input("Digite o preço do produto: R$ "))
percentual_desconto = float(input("Digite o desconto (%): "))
preco_final = calcular_desconto(preco_original, percentual_desconto)
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {percentual_desconto:.0f}%")
print(f"Preço final: R$ {preco_final:.2f}")
