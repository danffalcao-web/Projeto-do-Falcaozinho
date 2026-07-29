prêmios = ["Folha A1","Folha A2","Folha A3","Folha A4","Folha A5","Folha A6","Folha A7","Folha A8","Folha A9","Folha A10"]

print("Você tem 3 chances de conseguir o melhor prêmio")

import random

for i in range(3):
    prêmio = random.choice(prêmios)
    print(f"O prêmio que você tirou foi {prêmio}")
    if prêmio == "Folha A1":
        print("Você tirou o maior prêmio!")
        quit()
    else:
        escolha = input("Você quer tentar denovo? (sim ou não): ")
        if escolha == "sim":
            print("Bora lá")
        else:
            print("Ok")
            quit()
print("Suas chances acabaram, ficou sem prêmio")