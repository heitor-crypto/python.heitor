print("calcular o peso")
peso = float(input("digite o seu peso: "))
altura = float(input("digite a sua altura: "))
imc = peso / (altura ** 2)
print("seu imc é {:.2f}".format(imc))
if peso < 18.5 :
    print("abaixo do peso")
elif peso <= 18.5 < 24.9 :
    print("peso normal")
elif peso <= 25 < 34.9 :    
    print("sobrepeso")
else:
    print("acima do peso")
