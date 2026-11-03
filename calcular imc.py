
print("===== CALCULADORA DE IMC =====")

try:
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))

    if peso <= 0 or altura <= 0:
        print("Erro: peso e altura devem ser maiores que zero.")

    else:
        imc = peso / (altura ** 2)

        print(f"\nSeu IMC é: {imc:.2f}")

        if imc < 18.5:
            print("Classificação: Abaixo do peso")

        elif imc < 25:
            print("Classificação: Peso normal")

        elif imc < 30:
            print("Classificação: Sobrepeso")

        elif imc < 35:
            print("Classificação: Obesidade grau I")

        elif imc < 40:
            print("Classificação: Obesidade grau II")

        else:
            print("Classificação: Obesidade grau III")

except ValueError:
    print("Erro: digite valores numéricos válidos.")
