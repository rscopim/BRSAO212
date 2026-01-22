'''1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).'''

while True:
    try:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        operacao = input("Digite a operação a ser realizada (+, -, *, /): ")
        if operacao == "+":
            resultado = numero1 + numero2
        elif operacao == "-":
            resultado = numero1 - numero2
        elif operacao == "*":
            resultado = numero1 * numero2
        elif operacao == "/":
            resultado = numero1 / numero2
        else:
            print("Erro: operação inválida.\n")
            continue
        print("Resultado: ", resultado)
        break
    except ValueError:
        print("Erro: digite apenas números.\n")
    except ZeroDivisionError:
        print("Erro: não é permitido divisão por ZERO.\n")
