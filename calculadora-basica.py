while True:
    print("## caluculadora ##\n")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. resto da divisão")
    print("6. sair")
    escolha = input("Digite uma escolha: ")

    if escolha == "1":
        print("1. Soma")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print("a soma dos valores:", resultado,"\n")

    elif escolha == "2":
        print("2. Subtração")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print("a subtração dos valores:", resultado)

    elif escolha == "3":
        print("3. Multiplicação")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print("a multiplicação dos valores:", resultado)

    elif escolha == "4":
        print("4. Divisão")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 !=0:
            resultado = num1 / num2
            print("a divisão dos valores:", resultado)
        else:
            print("erro: divisão por zero. ")

    elif escolha == "5":
        print("5. resto da divisão")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 !=0:
            resultado = num1 % num2
            print("resto da divisão dos valores:", resultado)
        else:
            print("erro: divisão por zero. ")

    elif escolha == "6":
        print("6. sair")
        print("sair")
        break
    else:
        print("erro: escolha invalida. ")
