def verificar_senha(senha):
    # Critério A: verificar se tem pelo menos 8 caracteres
    if len(senha) < 8:
        return "Senha inválida: deve ter pelo menos 8 caracteres."
    
    # Critério B: verificar se contém pelo menos um número
    if not any(char.isdigit() for char in senha):
        return "Senha inválida: deve conter pelo menos um número."
    
    # Se passou nos dois critérios
    return "Senha válida!"

# Programa principal
senha_usuario = input("Digite sua senha: ")
resultado = verificar_senha(senha_usuario)
print(resultado)