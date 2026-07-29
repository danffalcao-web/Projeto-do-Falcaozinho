intervalo = int(input("Digite quantos números vão ser somados: "))
resultado = 0 
l = " "

for i in range(1,intervalo+1):
    numero = int(input("Digite um número para ser somado: "))
    
    resultado += numero
    l += str(numero)
    
    if i < intervalo:
        l += " + "
        if numero < 0:
            print("Não pode somar número negativo, a conta vai ser zerada")
            num = 0

print(f"{l} = {num}")
