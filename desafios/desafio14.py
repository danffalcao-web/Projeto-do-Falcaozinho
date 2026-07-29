n = float(input("Digite sua 1° nota: "))
n2 = float(input("Digite sua 2° nota: "))
n3 = float(input("Digite sua 1° nota: "))
m = float(input("Digite a média necessrária para você passar de ano: "))
sm = (n+n2+n3) / 3 

if sm >= m:
    print(f"Você passou de ano, sua média final é {sm}")
else:
    print(f"Você não passou de ano, sua média final é {sm}")