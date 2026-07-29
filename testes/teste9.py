import math

num1 = 400
num2 = 35

divisao = num1/num2
print(f"Divisão = {divisao}")

arredondamento = math.floor(divisao)
print(f"Arredondamento para menos =  {arredondamento}")

arredondamento2 = math.ceil(divisao)
print(f"Arredondamento para baixo = {arredondamento2}")

valor = 300

raizQuadrada = math.sqrt(valor)
print(F"Raiz Quadrada = {raizQuadrada}")

raizQuadrada2 = math.floor(math.sqrt(valor))
print(F"Raiz Quadrada Aproximada para menos = {raizQuadrada2}")

raizQuadrada3 = math.ceil(math.sqrt(valor))
print(F"Raiz Quadrada Aproximada para mais = {raizQuadrada3}")

pi = math.pi
print(f"Pi = {pi}")

import random

valor2 = random.randint(1,100)
print(f"Valor aleatório: {valor2}")

lista = ["a","b","c","dário"]

item = random.choice(lista)
print(f"Item aleatório na lista: {item}")