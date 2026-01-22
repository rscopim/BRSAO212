def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    gorjeta = (porcentagem_gorjeta / 100) * valor_conta
    return gorjeta

valor_conta = float(input("Digite o valor total da conta: R$ "))
porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta desejada (ex: 10 para 10%): "))
valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
print(f"O valor da gorjeta a ser deixada é: R$ {valor_gorjeta:.2f}")