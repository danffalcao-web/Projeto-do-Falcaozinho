n = input("Qual o nome do usuário? ")
s = input("Qual a senha da conta? ")
print("Cadastro feito com sucesso")

n2 = input("Confirme o nome do usuário: ")
s2 =input("Confirme a senha:")

if n==n2 and s==s2:
    print("Você fez o login")
else:
    print("Seu login foi bloqueado")