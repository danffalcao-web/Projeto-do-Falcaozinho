n = int(input("Digite um número:"))

if n >= 0 and n <= 10:
    print("Você digitou um número entre 0 e 10")
else:
    print("Você não digitou um número entre 0 e 10")

if n == 1 or n == 2:
    print("Você digitou um dos números secretos")
else:
    print("Você não digitou um dos números secretos")

if n > 0:
    print("Seu número é positivo")
elif n < 0:
    print("Seu número é negativo")
else:
    print("Seu número é neutro")