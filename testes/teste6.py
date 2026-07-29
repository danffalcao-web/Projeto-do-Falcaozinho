l = []

i = input("Digite um item para colocar na lista: ")
l.append(i)
print(l)
i2 = input("Digite outro um item para colocar na lista: ")
l.append(i2)
print(l)

i3 = input("Digite outro um item para colocar na lista: ")
i4 = input("Digite outro um item para colocar na lista: ")
l.extend([i3, i4])
print(l)

r = input("Digite qual item você quer deletar da lista: ")
l.remove(r)
print(l)

r2 = int(input("Digite o index do item que você quer remover: "))
l.pop(r2)
print(l)
