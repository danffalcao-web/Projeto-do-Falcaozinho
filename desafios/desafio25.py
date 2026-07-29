numero = int(input("Digite um intevalo de tempo: "))
l = []
lista = " "

for i in range(2,numero+1,2):
    l.append(i)
print(f"Os números pares desse intervalo são {l}")

for i in range(1,numero+1,2):
    #lista = lista + str(i) + " "
    #lista = lista + f"{i} "
    lista += str(i) + " "

print(f"Os números ímpares desse intervalo são {lista}")
