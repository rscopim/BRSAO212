while True:
        print("\nEscolha a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        escolha = input("Digite o número da operação respectiva: ")

        if escolha == '0':
            print("Saindo... Até logo!")
            break

        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if escolha == '1':
                    print(f"Resultado: {num1} + {num2} = {num1 + num2}")
                elif escolha == '2':
                    print(f"Resultado: {num1} - {num2} = {num1 - num2}")
                elif escolha == '3':
                    print(f"Resultado: {num1} * {num2} = {num1 * num2}")
                elif escolha == '4':
                    if num2 == 0:
                        print("Erro: Divisão por zero não é permitida!")
                    else:
                        print(f"Resultado: {num1} / {num2} = {num1 / num2}")
            except ValueError:
                print("Erro: Por favor, digite apenas números.")
        else:
            print("Opção inválida! Tente novamente.")