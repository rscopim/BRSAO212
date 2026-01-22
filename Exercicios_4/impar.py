'''4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.'''

pares = 0
impares = 0
quantidade = int(input("Digite a quantidade de números: "))
for i in range(quantidade):
    numero = int(input(f"Digite o número {i + 1}"))
    if numero % 2 == 0:
        pares += 1
        print(numero , ": é par")
    else:
        impares += 1
        print(numero , ": é impar")
print("Quantidade de números pares: ", pares)
print("Quantidade de números ímpares: ", impares)