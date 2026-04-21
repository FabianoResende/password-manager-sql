import random
import string

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True,
                usar_numeros=True, usar_simbolos=True):
    caracteres = ""

    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += "!@#$%^&*()-_=+[]{};:,.<>/?"

    if not caracteres:
        raise ValueError("Nenhum tipo de caractere selecionado.")

    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    print(gerar_senha())
