import random
import string

def gerar_senha(tamanho):
    if tamanho < 4:
        print("A senha deve ter pelo menos 4 caracteres.")
        return None

    # Conjuntos de caracteres
    letras = string.ascii_letters  # A-Z a-z
    digitos = string.digits        # 0-9
    simbolos = string.punctuation  # !@#$%&*()...

    # Garante pelo menos um de cada tipo
    senha = [
        random.choice(letras),
        random.choice(digitos),
        random.choice(simbolos),
        random.choice(letras + digitos + simbolos)
    ]

    # Preenche o restante da senha
    senha += random.choices(letras + digitos + simbolos, k=tamanho - 4)

    # Embaralha os caracteres
    random.shuffle(senha)

    return ''.join(senha)

# Entrada do usuário
try:
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    senha_gerada = gerar_senha(tamanho)
    if senha_gerada:
        print(f"🔐 Sua senha segura é: {senha_gerada}")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
