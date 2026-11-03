
print("===== EXERCÍCIO COM CONTINUE =====")

contador = 0

while contador < 40:
    contador += 1

    # Verifica se o número é múltiplo de 4
    if contador % 4 == 0:
        print("Pim")
        continue

    # Exibe os números que não são múltiplos de 4
    print(contador)

print("\nPrograma encerrado.")
