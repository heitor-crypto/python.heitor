# ferramenta continue
# a ferramenta continue no py vai interromper o loop,
# mas vai dar continuidade a ele

contador = 0

while contador <= 40:
    contador += 1

    # verifica se o valor de 'contador' é multiplicação de 4
    if (contador % 4 == 0):
        print("pim") # se for multiplo de 4, imprime "pim"
        continue # interrompe a iteração atual e volta para o início do loop

    # se o número não for multiplo de 4, imprime o valor do contador
    print(contador)

# após o término do loop, imprime a mensagem de finalização
print("acabou o programa")    
