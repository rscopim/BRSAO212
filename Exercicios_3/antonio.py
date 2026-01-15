'''def classificar_idade(idade):
    if 0 <= idade <= 12:
        return "Criança"
    elif 13 <= idade <= 17:
        return "Adolescente"
    elif 18 <= idade <= 59:
        return "Adulto"
    elif idade >= 60:
        return "Idoso"
    else:
        return "Idade inválida"

try:
    idade_usuario = int(input("Digite sua idade: "))
    categoria = classificar_idade(idade_usuario)
    print(f"Você é classificado como: {categoria}")
except ValueError:
    print("Por favor, digite um número válido para a idade.")'''

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    celsius = fahrenheit_para_celsius(f)
    return celsius_para_kelvin(celsius)

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    celsius = kelvin_para_celsius(k)
    return celsius_para_fahrenheit(celsius)

def main():
    try:
        temp = float(input("Digite a temperatura: "))
        unidade_origem = input("Digite a unidade de origem (Celsius, Fahrenheit, Kelvin): ").strip().lower()
        unidade_destino = input("Digite a unidade de destino (Celsius, Fahrenheit, Kelvin): ").strip().lower()

        resultado = None

        if unidade_origem == unidade_destino:
            resultado = temp
        elif unidade_origem == "celsius":
            if unidade_destino == "fahrenheit":
                resultado = celsius_para_fahrenheit(temp)
            elif unidade_destino == "kelvin":
                resultado = celsius_para_kelvin(temp)
        elif unidade_origem == "fahrenheit":
            if unidade_destino == "celsius":
                resultado = fahrenheit_para_celsius(temp)
            elif unidade_destino == "kelvin":
                resultado = fahrenheit_para_kelvin(temp)
        elif unidade_origem == "kelvin":
            if unidade_destino == "celsius":
                resultado = kelvin_para_celsius(temp)
            elif unidade_destino == "fahrenheit":
                resultado = kelvin_para_fahrenheit(temp)

        if resultado is not None:
            print(f"{temp}° {unidade_origem.capitalize()} é igual a {resultado:.2f}° {unidade_destino.capitalize()}.")
        else:
            print("Unidades de conversão inválidas. Por favor, escolha entre Celsius, Fahrenheit e Kelvin.")

    except ValueError:
        print("Entrada de temperatura inválida. Por favor, insira um número.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()