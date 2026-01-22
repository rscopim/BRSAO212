def calculadora():
    print("=== Calculadora Básica ===")
    print("Operações disponíveis: +, -, *, /")

    # Entrada dos números
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    # Estrutura condicional para escolher a operação
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 != 0:  # Evita divisão por zero
            resultado = num1 / num2
        else:
            return "Erro: divisão por zero não é permitida!"
    else:
        return "Operação inválida!"

    return f"Resultado: {resultado}"


# Executando a calculadora
print(calculadora())