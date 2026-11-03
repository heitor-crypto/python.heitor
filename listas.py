
numeros = []

print("===== ANÁLISE DE NÚMEROS =====")

for i in range(5):
    while True:
        try:
            num = int(input(f"Digite o {i + 1}º número: "))
            numeros.append(num)
            break

        except ValueError:
            print("Erro: digite um número inteiro válido.")

maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = soma / len(numeros)

print("\n===== RESULTADOS =====")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Soma dos números: {soma}")
print(f"Média dos números: {media:.2f}")
