n = input("Qual seu nome: ")
i = int(input("Quantos anos você tem: "))

if i >= 18:
    print(f"{n}, você pode entrar no bar")
else:
    print(f"{n}, você é uma criança, vai embora do bar")