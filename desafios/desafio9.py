v1 = float(input("Digite o valor de um produto: "))
v2 = float(input("Digite o valor de um produto: "))
v3 = float(input("Digite o valor de um produto: "))

soma = v1 + v2 + v3
visao = soma / 1.05
credito = soma * 1.078

print(f"O total da sua compra deu {soma} reais")
print("Temos 3 possibilidades de pagamento: à vista, débito e crédito")
print(f"Caso você pague à vista ficará {visao} reais")
print(f"Se for pagar por crédito ficará {credito} reais")
print(f"Caso pague por débito o valor não mudará ele continuará sendo {soma} reais")