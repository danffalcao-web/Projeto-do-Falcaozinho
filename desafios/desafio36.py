def bytes(quantidade):
    #1 Megabyte = 1024 kilobytes
    kiby = quantidade * 1024
    return kiby
def distancia(quantidade):
    #1 Km = 1000 m
    m = quantidade * 1000
    return m 
def liquido(quantidade):
    #1L = 1000 ml
    ml = quantidade * 1000
    return ml
def temperatura(quantidade):
    #0°C = 32 Fahrenheit
    fah = (quantidade * 9/5) + 32
    return fah
def dinheiro(quantidade):
    #1 $ = 5,18 R$
    real = quantidade * 5.20
    return real
def peso(quantidade):
    #1 Tonelada = 1000 Kg
    kilo = quantidade * 1000
    return kilo

print("|CONVERSÕES|")

while True: 
    print("="*40)
    print("As conversões são:")
    print("Bytes: Megabytes -> Kilobytes")
    print("Distancia: Kilometros -> Metros")
    print("Liquido: Litros -> Mililitros")
    print("Temperatura: Celsius -> Fahrenheit")
    print("Dinheiro: Dólar -> Real")
    print("Peso: Toneladas -> Kilogramas")
    print("="*40)

    conversão = input("Digite qual tipo de conversão você quer fazer(digite sair caso queira parar)? ")
    quantidade = int(input("Digite a quantidade que você quer transformar(digite 0 caso queira sair): "))
    print("="*40)

    if quantidade == 0 or conversão == "sair":
        break
    if conversão == "bytes":
        b = bytes(quantidade)
        print(f"{quantidade} megabytes = {b} kilobytes")
    elif conversão == "distancia":
        dt = distancia(quantidade)
        print(f"{quantidade} kilometros = {dt} metros")
    elif conversão == "liquido":
        l = liquido(quantidade)
        print(f"{quantidade} litros = {l} mililitros")
    elif conversão == "temperatura":
        t = temperatura(quantidade)
        print(f"{quantidade} celsius = {t} fahrenheit")
    elif conversão == "dinheiro":
        dh = dinheiro(quantidade)
        print(f"{quantidade} dolares = {dh} reais")
    elif conversão == "peso":
        p = peso(quantidade)
        print(f"{quantidade} toneladas = {p} kilogramas")
    elif conversão == "sair":
        break
    else:
        print("Não tem essa conversão")