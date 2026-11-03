
print("===== CONTROLE DE FLUXO =====")

contador = 0

while contador < 40:
    contador += 1

    if contador == 6:
        print("Número 6 ignorado.")
        continue

    if 10 <= contador <= 27:
        continue

    print(contador)

print("\nPrograma encerrado ao chegar ao número 40.")
