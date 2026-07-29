l = ["Lápis", "lapiseira", "borracha", "grafite", "apontador"]

print(l)
print("Estas são as últimas unidades desses produtos.")

p = int(input("Qual deles você quer? (contando que lápis é 0, lapiseira é 1...): "))

print(f"Você escolheu o produto '{l[p]}'")

l[p] = "esgotado"

print("Agora nossa lista de produtos está assim:")
print(l)