n = input("Qual seu nome? ")
i = int(input("Qual sua idade? "))
c = input("Você tem um convite, sim ou não? ")

if i >= 18 and c == "sim":
    print(f"{n} sua entrada tá permitida")
elif i < 18 and c == "não":
    print(f"Tu não tem nada também,{n}")
elif i < 18:
    print(f"Largaram uma criança {n} na porta da festa")
elif c == "não":
    print(f"{n} sua entrada não tá permitida")
else:
    print("oxe")