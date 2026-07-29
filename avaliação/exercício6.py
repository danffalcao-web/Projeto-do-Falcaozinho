a = float(input("Digite quantos minutos se passaram desde que você sofreu com matemática: "))
b = a / 60
c = b / 24

if c < 1:
    print(f"Nem foi 1 dia, foi {c} dias")
elif c == 1:
    print("Carambolas, foi exatos 1 dia")
else:
    print(f"Faz um tempão então, foi {c} dias")
    