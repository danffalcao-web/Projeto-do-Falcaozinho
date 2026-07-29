palavra = input("Digite uma palavra: ")
contagem = 0

for i in palavra:
    contagem += 1

print(f"{palavra} têm {contagem} dígitos")