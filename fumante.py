dia = int(input("Quantos cigarros você fuma por dia? "))
anos= int(input("Quantos anos você já fuma? "))

# Calculando o número total de cigarros fumados.
total = dia * 365 * anos

# Calculando a redução total do tempo de vida em minutos.
reducaominutos = total * 10

# Calculando a redução total do tempo de vida em dias.
reducaodias = reducaominutos // (24 * 60)

# Exiba o total em dias.
print("Você perderá", reducaodias, "dias de vida.")
