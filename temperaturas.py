
def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32


def kelvin_to_celsius(k):
    return k - 273.15


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def celsius_to_kelvin(c):
    return c + 273.15


def menu():
    print("\n===== CONVERSOR DE TEMPERATURAS =====")
    print("1. Fahrenheit para Kelvin")
    print("2. Fahrenheit para Celsius")
    print("3. Kelvin para Fahrenheit")
    print("4. Kelvin para Celsius")
    print("5. Celsius para Fahrenheit")
    print("6. Celsius para Kelvin")
    print("7. Sair")


while True:
    menu()
    opcao = input("\nEscolha uma opção: ")

    if opcao == "7":
        print("Programa encerrado.")
        break

    if opcao not in ["1", "2", "3", "4", "5", "6"]:
        print("Erro: opção inválida.")
        continue

    try:
        temperatura = float(input("Digite a temperatura: "))

    except ValueError:
        print("Erro: digite um número válido.")
        continue

    # Verifica temperaturas abaixo do zero absoluto
    if opcao in ["1", "2"] and temperatura < -459.67:
        print("Erro: temperatura abaixo do zero absoluto.")
        continue

    if opcao in ["3", "4"] and temperatura < 0:
        print("Erro: Kelvin não pode ser negativo.")
        continue

    if opcao in ["5", "6"] and temperatura < -273.15:
        print("Erro: temperatura abaixo do zero absoluto.")
        continue

    if opcao == "1":
        resultado = fahrenheit_to_kelvin(temperatura)
        unidade = "K"

    elif opcao == "2":
        resultado = fahrenheit_to_celsius(temperatura)
        unidade = "°C"

    elif opcao == "3":
        resultado = kelvin_to_fahrenheit(temperatura)
        unidade = "°F"

    elif opcao == "4":
        resultado = kelvin_to_celsius(temperatura)
        unidade = "°C"

    elif opcao == "5":
        resultado = celsius_to_fahrenheit(temperatura)
        unidade = "°F"

    else:
        resultado = celsius_to_kelvin(temperatura)
        unidade = "K"

    print(f"Resultado: {resultado:.2f} {unidade}")
