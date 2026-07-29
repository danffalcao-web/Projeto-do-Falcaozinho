n = input("Olá, qual seu nome? ")
t = input(f"{n}, você quer trabalhar aqui, sim ou não? ")

if t == "sim":
    print("Então vamos continuar")
    
    c = input(f"{n}, você está com o currículo, sim ou não? ")

    if c == "sim":
        print("Então vamos começar a entrevista")
    else:
        print("Vai embora")
else:
    print("Vai embora")



