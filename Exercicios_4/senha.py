'''3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.'''

senha = input("Digite a senha, ela precisa conter pelo menos 8 caracteres e 1 número: ")
tamanho_minimo = len(senha) >= 8
contem_numero = any(caractere.isdigit() for caractere in senha)
if tamanho_minimo and contem_numero:
    print("Senha válida.")
else:
    print("Senha inválida.")

