
print("===== GERADOR DE TABUADA =====")

try:
    numero = int(input("Digite um número inteiro: "))

    print(f"\nTabuada do {numero}:\n")

    contador = 1

    while contador <= 10:
        resultado = numero * contador
        print(f"{numero} x {contador} = {resultado}")
        contador += 1

except ValueError:
    print("Erro: digite um número inteiro válido.")
