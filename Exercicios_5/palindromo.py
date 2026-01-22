'''2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.'''

def e_palindromo(texto: str) -> bool:
    texto_limpo = "".join(caractere.lower() for caractere in texto if caractere.isalnum())
    return texto_limpo == texto_limpo[::-1]
frase = input("Digite uma frase ou uma palavra: ")
resultado = e_palindromo(frase)
print(f"Resultado: {"Sim" if resultado else "Não"}")