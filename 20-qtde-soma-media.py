soma = 0
contador = 0

while True:
    numero = int(input ("digite um numero para (0 para sair): "))
    if numero == 0:
        break
    
    soma += numero
    contador += 1

if contador > 0:
        media = soma / contador

        print(f"quantidade de numeros digitador: {contador}")
        print(f"soma dos numeros digitados: {soma}")
        print(f"media aritimetica: {media}")
else:
        print("nenhum numero foi digitado.")
