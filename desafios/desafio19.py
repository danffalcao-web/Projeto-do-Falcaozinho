n = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
m = input("Qual método vai querer? (+ ou - ou * ou / ou **): ")

if m == "+":
    r = n + n2
elif m == "-":
    r = n - n2
elif m == "*":
    r = n * n2
elif m == "/":
    r = n / n2
elif m == "**":
    r = n ** n2
else:
    r = False

if r == False:
    print("Error - Método inexistente ou não encontrado no programa")
else:
    print(f"{n} {m} {n2} = {r}") 