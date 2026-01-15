# Conversor de Temperatura
temp = float(input("Digite a temperatura: "))  # Solicita a temperatura ao usuário
origem = input("Digite a unidade de origem (C para Celsius, F para Fahrenheit, K para Fahrenheit): ").upper() # Solicita a unidade de origem da temperatura
destino = input("Digite a unidade de destino (C para Celsius, F para Fahrenheit, K para Fahrenheit): ").upper()  # Solicita a unidade de destino da temperatura
if origem == "C" and destino == "F":
    resultado = (temp * 9/5) + 32
elif origem == "C" and destino == "K":
    resultado = temp + 273.15
elif origem == "F" and destino == "C":
    resultado = (temp - 32) * 5/9
elif origem == "F" and destino == "K":
    resultado = (temp - 32) * 5/9 + 273.15
elif origem == "K" and destino == "C":
    resultado = temp - 273.15
elif origem == "K" and destino == "F":
    resultado = (temp - 273.15) * 9/5 + 32
elif origem == destino:
    resultado = temp  # Mesma unidade, sem conversão
else:
    resultado = None  # Unidade inválida
if resultado is not None:
    print(f"{temp} {origem} é igual a {resultado:.2f} {destino}")  # Exibe o resultado formatado com duas casas decimais
else:
    print("Unidade inválida. Use C, F ou K.")  # Mensagem de erro para unidade inválida