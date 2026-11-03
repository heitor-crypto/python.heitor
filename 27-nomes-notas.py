
nomes = []
notas = []

print("===== CADASTRO DE ALUNOS =====")

for i in range(5):
    nome = input(f"\nDigite o nome do {i + 1}º aluno: ").strip()

    while not nome:
        print("Erro: o nome não pode ficar vazio.")
        nome = input("Digite o nome do aluno: ").strip()

    while True:
        try:
            nota = float(input(f"Digite a nota de {nome}: "))

            if 0 <= nota <= 10:
                break
            else:
                print("Erro: a nota deve estar entre 0 e 10.")

        except ValueError:
            print("Erro: digite uma nota numérica válida.")

    nomes.append(nome)
    notas.append(nota)

print("\n===== DADOS DOS ALUNOS =====")

for i in range(len(nomes)):
    print(f"{i + 1}. Nome: {nomes[i]} | Nota: {notas[i]:.1f}")

media = sum(notas) / len(notas)

print(f"\nMédia geral da turma: {media:.1f}")
