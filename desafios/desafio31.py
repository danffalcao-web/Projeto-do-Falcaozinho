lista = ["Sim","Isso","É","Nome","De","Usuário"]
for i in range(3):
    chance = input("Digite um nome de usuário: ")
    if chance in lista:
        print("Você acertou")
        break
    elif i >= 2:
        print("Você errou 3 vezes, o código se encerrará")
        quit()
    

print("Agora que você passou, uma pergunta")

nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))
nota3 = float(input("Digite a 3° nota: "))

media_final = (nota1+nota2+nota3) / 3
        
print(f"Sua média final é {media_final}")