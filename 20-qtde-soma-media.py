
soma = 0
contador = 0

print("===== SOMA E MÉDIA DE NÚMEROS =====")
print("Digite 0 para encerrar o programa.\n")

while True:
    try:
        numero = int(input("Digite um número inteiro: "))

        if numero == 0:
            break

        soma += numero
        contador += 1

    except ValueError:
        print("Erro: digite um número inteiro válido.")

print("\n===== RESULTADOS =====")

if contador > 0:
    media = soma / contador

    print(f"Quantidade de números digitados: {contador}")
    print(f"Soma dos números digitados: {soma}")
    print(f"Média aritmética: {media:.2f}")

else:
    print("Nenhum número foi digitado.")
