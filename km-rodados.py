
print("===== CALCULADORA DE ALUGUEL DE CARRO =====")

try:
    km_rodados = float(input("Quantos quilômetros foram rodados? "))
    dias = int(input("Por quantos dias o carro foi alugado? "))

    if km_rodados < 0 or dias <= 0:
        print("Erro: informe uma quilometragem válida e pelo menos um dia de aluguel.")

    else:
        valor_diarias = 60 * dias
        valor_km = 0.15 * km_rodados
        valor_total = valor_diarias + valor_km

        print("\n===== RESUMO DO ALUGUEL =====")
        print(f"Quantidade de dias: {dias}")
        print(f"Quilômetros rodados: {km_rodados:.2f} km")
        print(f"Valor das diárias: R$ {valor_diarias:.2f}")
        print(f"Valor da quilometragem: R$ {valor_km:.2f}")
        print(f"Total a pagar: R$ {valor_total:.2f}")

except ValueError:
    print("Erro: digite valores numéricos válidos.")
