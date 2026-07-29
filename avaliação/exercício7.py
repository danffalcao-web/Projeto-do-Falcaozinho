a = float(input("Digite quantas horas você trabalhou: "))
b = int(input("Digite quantas tarefas você fez: "))

if a >= 5 and b >= 4:
    print("Você fez o mínimo")
elif a < 5 and b >= 4:
    print("Você foi produtivo, mas vai ter que comprir horário")
else:
    print("Vai ter que fazer hora-extra")