numero = int(input("Digite um intevalo: "))
resultado = 0
l = " "

for i in range(1,numero+1):
    resultado += i
    l += str(i)
    if i < numero:
        l += " + "

print(f"{l} = {resultado}")
