import random
perguntas = ["Qual a cor da maçã verde? ","Um Fiat Uno com escada é mais rápido que um jato? ","Qual o melhor jogo que já existiu? ","Vai ter gartic nessa semana? "]
respostas = ["Verde","Sim","O jogo do cachorrinho","Vai"]
erros = 0

print("Digite 'desistir' se não souber")
pergunta = random.randint(0,3)

while True:
    print(perguntas[pergunta])
    resposta = input("Qual a resposta?: ")

    if respostas[pergunta] == resposta:
        print("top")
        if erros > 0:
            print(f"Errou {erros}")
        else:
            print("Sem erros. 10/10")
        break
    elif resposta == "desisto":
        print(f"A resposta era {respostas[pergunta]}")

        break
    else:
        print("Nah")
        erros += 1