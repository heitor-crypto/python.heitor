kmrodados = float(input("quantos km foram rodados? "))
dias = int(input("por quantos dias o carro foi usado? "))

valor = (60 + dias) * (0.15 + kmrodados)
print(f"o valor a pagar pelo aluguel do carro é {valor}")
