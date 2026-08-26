import random

def ViniSênior():
    prêmios = ["Folha A1","Folha A2","Folha A3","Folha A4","Folha A5","Folha A6","Folha A7","Folha A8","Folha A9","Folha A10"]

    print("Você tem 3 chances de conseguir o melhor prêmio")

    for i in range(3):
        prêmio = random.choice(prêmios)
        print(f"O prêmio que você tirou foi {prêmio}")
        if prêmio == "Folha A1":
            print("Você tirou o maior prêmio!")
            break
        else:
         escolha = input("Você quer tentar denovo? (sim ou não): ")
        if escolha == "sim":
            print("Bora lá")
        else:
            print("Ok")
            break
    print("Suas chances acabaram, ficou sem prêmio")

def Nutricionista():
    l = ["banana", "maçã", "laranja", "kiwi", "melancia", "melão", "mamão", "pêssego", "pitaya", "abacate", "tomate", "caqui", "romã", "acerola", "limão", "atemoia", "coco", "morango", "maracujá", "jabuticaba", "pera", "lichia", "jaca", "uva", "pitanga", "mexirica", "abacaxi", "manga", "amora", "maçã verde", "mirtilo", "framboesa", "cereja", "goiaba", "guaraná", "açaí", "cupuaçu", "caju", "carambola", "cacau", "damasco", "figo", "graviola", "nectarina", "tangerina", "tamarindo", "yamamomo", "pepino", "abóbora", "zimbro"]

    print(f"Essa é uma lista de frutas: {l}")

    f = int(input("Entre essas frutas, qual é a sua favorita?(Considerando que a banana é 0, maçã é 1...): "))

    print(f"Então sua fruta favorita é {l[f]}, você tem bom gosto")

while True:
    escolha = int(input("Você quer a função 1 ou 2? "))
    if escolha == 1:
        ViniSênior()
    elif escolha == 2: 
        Nutricionista()
    else:
        print("Não tem essa função")