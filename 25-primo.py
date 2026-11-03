
from math import isqrt


def eh_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, isqrt(numero) + 1):
        if numero % i == 0:
            return False

    return True


try:
    num = int(input("Digite um número inteiro: "))

    if eh_primo(num):
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")

except ValueError:
    print("Erro: digite um número inteiro válido.")
