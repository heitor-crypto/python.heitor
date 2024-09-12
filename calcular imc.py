print("calcular o peso")
peso = float(input("digite o seu peso: "))
altura = float(input("digite a sua altura: "))
imc = peso / (altura ** 2)
print("seu imc é {:.2f}".format(imc))
if (peso <= 18,5 ):
    print("abaixo do peso")
elif (peso in 18.5 and 24.9):
    print("peso normal")
else:
    print("acima do peso")
