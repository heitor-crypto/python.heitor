
while True:
    print("\n===== CALCULADORA =====")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Resto da divisão")
    print("6. Sair")

    escolha = input("\nDigite uma opção: ")

    if escolha == "6":
        print("Calculadora encerrada.")
        break

    if escolha not in ["1", "2", "3", "4", "5"]:
        print("Opção inválida. Tente novamente.")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

    except ValueError:
        print("Erro: digite apenas números válidos.")
        continue

    if escolha == "1":
        resultado = num1 + num2
        print(f"Resultado da soma: {resultado}")

    elif escolha == "2":
        resultado = num1 - num2
        print(f"Resultado da subtração: {resultado}")

    elif escolha == "3":
        resultado = num1 * num2
        print(f"Resultado da multiplicação: {resultado}")

    elif escolha == "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Erro: não é possível dividir por zero.")

    elif escolha == "5":
        if num2 != 0:
            resultado = num1 % num2
            print(f"Resto da divisão: {resultado}")
        else:
            print("Erro: não é possível dividir por zero.")
