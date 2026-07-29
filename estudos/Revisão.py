print("Bem-vindo ao jogo 'RNG da Copa'")
print("Há 4 categorias para desbloquear")
print("A cada categoria descoberta fica mais dificil encontrar os novos paises")
print("Encontre todos os paises da copa")
print("")
estreantes = ["Uzbequistão", "Cabo Verde", "Curaçao", "Jordânia"]
diversos = ["México","África do Sul","Coreia do Sul","República Tcheca","Canadá","Bósnia e Hezergovina","Suíça","Qatar","Haiti","Escócia","Estados Unidos da América","Austrália","Paraguai","Turquia","Japão","Suécia","Tunisía","Curaçao","Equador","Costa do Marfim","Irã","Nova Zelândia","Senegal","Iraque","Arábia Saudita","Austria","Algéria","Jordânia","República Democrática do Congo","Uzbequistão","Panamá","Gana"]
campeoes = ["México","África do Sul","Coreia do Sul","República Tcheca","Canadá","Bósnia e Hezergovina","Suíça","Qatar","Brasil","Haiti","Marrocos","Escócia","Estados Unidos da América","Austrália","Paraguai","Turquia","Japão","Holanda","Suécia","Tunisía","Alemanha","Curaçao","Equador","Costa do Marfim","Bélgica","Egito","Irã","Nova Zelândia","França","Senegal","Noruega","Iraque","Espanha","Cabo Verde","Arábia Saudita","Uruguai","Argentina","Austria","Algéria","Jordânia","Portugal","República Democrática do Congo","Uzbequistão","Colômbia","Croácia","Inglaterra","Panamá","Gana"]
potencias = ["México","África do Sul","Coreia do Sul","República Tcheca","Canadá","Bósnia e Hezergovina","Suíça","Qatar","Haiti","Marrocos","Escócia","Estados Unidos da América","Austrália","Paraguai","Turquia","Japão","Holanda","Suécia","Tunisía","Curaçao","Equador","Costa do Marfim","Bélgica","Egito","Irã","Nova Zelândia","Senegal","Noruega","Iraque","Cabo Verde","Arábia Saudita","Austria","Algéria","Jordânia","Portugal","República Democrática do Congo","Uzbequistão","Colômbia","Croácia","Panamá","Gana"]

import random

print("Você está na categoria 'Estreantes'")
print("Gire 10 vezes para desbloquear outra categoria")
for i in range(1,10+1):

    rng1 =random.choice(estreantes)
    print(f"{i}° país: {rng1}")

    print("Aperte enter para gerar um novo ou digite 'sair'...")
    escolha = input("")
    
    if escolha == "sair":
        break

print("Você está na categoria 'Diversos'")
print("Gire mais 20 vezes para desbloquear outra categoria")

for i in range(11,30+1):

    rng2 =random.choice(diversos)
    print(f"{i}° país: {rng2}")

    print("Aperte enter para gerar um novo ou digite 'sair'...")
    escolha = input("")
        
    if escolha == "sair":
        break

print("Você está na categoria 'Potências'")
print("Gire mais 30 vezes para desbloquear outra categoria")

for i in range(31,60+1):

    
    rng3 =random.choice(potencias)
    print(f"{i}° país: {rng3}")
    
    print("Aperte enter para gerar um novo ou digite 'sair'...")
    escolha = input("")
            
    if escolha == "sair":
        break
print("Você está na última categoria 'Campeões Mundiais'")
print("Consiga todos os países que participaram na copa de 2026")

for i in range(61,10000000000000000):
    
    rng4 =random.choice(campeoes)
    print(f"{i}° país: {rng4}")
    
    print("Aperte enter para gerar um novo ou digite 'sair'...")
    escolha = input("")
            
    if escolha == "sair":
        break