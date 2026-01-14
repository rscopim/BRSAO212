'''1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.'''

valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro
print(f"Valor em reais: R$ {valor_reais:.2f}") # A formatação :.2f serve para deixar o numero com 2 casas decimais
print("Valor em dólares: $", round(valor_dolar, 2)) # A formatação ROUND serve para arredondar para 2 casas decimais
print(f"Valor em euros: € {valor_euro:.3f}")
