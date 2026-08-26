numero = 0

while numero == 0:
    numero = int(input("Digite um número sem ser 0: "))
print("Acabou a repetição")

while True:
    escolha = input("Digite 'abacaxi' para quebrar a repetição: ")

    if escolha == 'abacaxi':
        break
print("Acabou a repetição, de novo")
