numeros = []
for i in range(5):
    num = int(input(f"Digite o {i +1}º número: "))
    numeros.append(num)
    
maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)

print("Maior numero:", maior)
print("Menor numero:", menor)
print("Soma dos numeros:", soma) 
