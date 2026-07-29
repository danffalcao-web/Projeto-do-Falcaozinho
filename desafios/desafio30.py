print("Esse é o Z-Typer falsificado")

palavras = ["banana","ananab","banana ao contrário", "contrário a banana","oiràrtnoc a ananab", "ananab ao oiràrtnoc"]
pontos = 0
sotnop = 0

for i in palavras:
    pergunta = input(f"Digite a palavra '{i}': ")
    if pergunta == i:
        print("Ganhou 1 ponto")
        pontos += 1
    else:
        print("Errou")
        sotnop += 1

if sotnop == 0:
    print(f"Você acertou tudo, boa")
elif pontos == 0: 
    print(f"Você errou todas, boa")
else:
    print(f"Você acertou {pontos} palavras, boa")
