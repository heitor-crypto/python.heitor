
print("===== VERIFICADOR DE VOTO =====")

try:
    idade = int(input("Digite sua idade: "))

    if idade < 0:
        print("Erro: a idade não pode ser negativa.")

    elif idade < 16:
        print("Você ainda não tem idade para votar.")

    elif idade < 18 or idade >= 70:
        print("Seu voto é facultativo.")

    else:
        alfabetizado = input(
            "Você sabe ler e escrever? (s/n): "
        ).strip().lower()

        if alfabetizado == "s":
            print("Seu voto é obrigatório.")

        elif alfabetizado == "n":
            print("Seu voto é facultativo.")

        else:
            print("Erro: responda apenas s ou n.")

except ValueError:
    print("Erro: digite uma idade válida.")
