print("bem vindo a câmara secreta")

idade = int(input("Digite a sua idade: "))

if idade >= 18  and idade < 65: 
    print("voto obrigatório")
elif idade >= 16 and idade <17 or idade>=65: 
    print("voto opcional")
else :
    print("você não pode votar")
