nome = "Danilo"
idade = 14
altura = 1.60
trabalha = False
calculo = 1+2

print("Meu nome é", nome)
print("Eu tenho",idade,"anos")
print(f"Eu tenho {altura} metros de altura")
print(f"Minha situação de trabalho é {trabalha}")
print(f"1+2 = {calculo}")

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")

print(f"Seu nome é {nome}, sua idade é {idade} anos, sua altura é {altura} metros")

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
nomeCompleto = nome + " " + sobrenome
print(f"Seu nome completo é {nomeCompleto}")

numero1 = int(input("Digite o número 1: "))
numero2 = int(input("Diigite o número 2: "))
soma = numero1 + numero2
print(f"{numero1} + {numero2} = {soma}")