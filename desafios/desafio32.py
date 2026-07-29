lados = int(input("Digite quantos lados seu dado vai ter: "))

import random 

for i in range(1000000000):
    dado = random.randint(1,lados)
    print(f"Dado [D{lados}]: {dado}")

    print("Aperte enter para gerar um novo ou digite 'sair'...")
    escolha = input("")

    if escolha == "sair":
        break