par = 0
impar = 0
quantidade = int(input("Quantos números você deseja analisar? "))
for i in range(quantidade):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        par += 1
        print(f"O número {num} é par.")
    else:
        impar += 1
        print(f"O número {num} é ímpar.")
print(f"Total de números pares: {par}")
print(f"Total de números ímpares: {impar}")