p = float(input("Qual é a sua pontuação no ranking de um jogo, não dá pra ser menor que 0? "))

if p == 0:
    print("Você nem jogou ainda")
elif p >= 1 and p <= 200:
    print("Você é iniciante")
elif p >= 201 and p <= 500:
    print("Você é veterano")
elif p >= 501 and p <= 700:
    print("Você é mestre")
elif p >= 701 and p <= 1000:
    print("Você é campeão")
else:
    print("Você é lendário")