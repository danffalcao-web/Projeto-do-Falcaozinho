a = input("Digite o nome do 1° produto: ")
a1 = float(input("Digite o valor desse produto: "))
b = input("Digite o nome do 2° produto: ")
b1 = float(input("Digite o valor desse produto: "))
c = input("Digite o nome do 3° produto: ")
c1 = float(input("Digite o valor desse produto: "))
d = a1 + b1 + c1

print(f"O primeiro produto foi {a}, custando {a1} reais")
print(f"O primeiro produto foi {b}, custando {b1} reais")
print(f"O primeiro produto foi {c}, custando {c1} reais")
print(f"O total da compra é {d} reais")

e = input("Dá pra parcelar em 4x, 6x ou 12x sem juros, você quer parcelar?(sim ou não): ")

if e == "sim":
    f = int(input("Você quer parcelar em 4x, 6x ou 12x sem juros?(Escreva só o número): "))
    if f == 4:
        g = d / 4
        print(f"Você vai pagar 4 parcelas de {g} reais")
    elif f == 6:
        h = d / 6
        print(f"Você vai pagar 6 parcelas de {h} reais")
    elif f == 12:
        i = d / 12
        print(F"Você vai pagar 12 parcelas de {i} reais")
    else:
        print("Não dá pra parcelar nesse valor")
else:
    print("Obrigado pela compra")