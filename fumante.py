
print("===== ESTIMATIVA DIDÁTICA SOBRE TABAGISMO =====")

try:
    cigarros_dia = int(input("Quantos cigarros você fuma por dia? "))
    anos = int(input("Há quantos anos você fuma? "))

    if cigarros_dia < 0 or anos < 0:
        print("Erro: os valores não podem ser negativos.")

    else:
        # Hipótese didática: 10 minutos por cigarro
        minutos_por_cigarro = 10

        # Estimativa do total de cigarros
        total_cigarros = cigarros_dia * 365 * anos

        # Cálculo hipotético em minutos e dias
        reducao_minutos = total_cigarros * minutos_por_cigarro
        reducao_dias = reducao_minutos / (24 * 60)

        print("\n===== RESULTADOS =====")
        print(f"Total estimado de cigarros: {total_cigarros}")
        print(f"Tempo hipotético equivalente: {reducao_dias:.1f} dias")

        print("\nAtenção: este cálculo é apenas um exercício")
        print("matemático e não prevê a expectativa de vida.")

except ValueError:
    print("Erro: digite apenas números inteiros válidos.")
