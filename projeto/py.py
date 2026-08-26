print("-"*40)
print("|SISTEMA BANCÁRIO|")
print("-"*40)
print("Bem Vindo ao Banco de Madeira")
nome = input("Digite o seu nome: ")
saldo = float(input(f"{nome}, digite seu saldo bancário, não digite número negativo: "))

if saldo < 0:
    print("Complicado.")
else:
    while True:
        print("-"*40)
        depositoousaqueousair = input(f"{nome}, você quer depositar ou sacar dinheiro ou sair da conta do banco? ")
        if depositoousaqueousair == "sacar":
            saque = float(input(f"{nome}, digite quanto você quer sacar, não digite número negativo: "))
            if saque < 0:
                print("Não é possível sacar um valor negativo")
            elif saque > saldo:
                print("Não é possível sacar um valor que você não tenha")
            else:  
                saldo-=saque
                print(f"{nome}, seu saldo é de R${saldo}")           
        elif depositoousaqueousair == "depositar": 
            deposito = float(input(f"{nome}, digite quanto você quer depositar, não digite número negativo: "))
            if deposito < 0: 
                print("Não é possível depositar um valor negativo")
            else:
                saldo+=deposito
                print(f"{nome}, seu saldo é de R${saldo}")  
        elif depositoousaqueousair == "sair":
            print("Volte sempre!")
            break
        else:
            print("Não temos essa função, talvez o Banco de Pedra tenha.")
