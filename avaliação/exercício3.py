a = float(input("Digite, em cm, a medidia da base de um retângulo deitado: "))
b = float(input("Digite, em cm, a medidia da altura de um retângulo deitado: "))
ar = a * b
p = (2*a) + (2*b)
df = a - b
di = (a**2 + b**2)**0.5

print(f"A área do retângulo é {ar}cm²")
print(f"O perímetro do retângulo é {p}")
print(f"A diferença do retângulo é {df}")
print(f"A diagonal do retângulo é {di}")