a = float(input("Digite quanto de dinheiro você tem: "))
b = float(input("Digite, em litros, a quantidade de gasolina que você colocou no carro: "))
c = float(input("Digite o valor do litro da gasolina: "))
d = b * c

print(f"Ficou {d} reais")

if d <= a:
    print("Você consegue pagar")
else: 
    print("Devolve a gasolina")