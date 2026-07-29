l = ["cléber", "clebinho", "clebão", "cleboa", "clebinha"]

print(l)
print("Esses são os alunos de uma sala de aula")

x = input("Digite o nome de outro aluno para entrar na sala: ")
y = input("Digite o nome de outro aluno para entrar na sala: ")
z = input("Digite o nome de outro aluno para entrar na sala: ")
l.extend([x,y,z])

print(l)

r = input("Remova um aluno da turma pelo nome: ")
l.remove(r)

print(l)

p = input("Você deseja alterar o nome de um aluno na lista? (sim ou não): ")

if p == "sim":
   a = int(input("Digite o index do aluno que deseja alterar o nome: "))
   c = input("Digite o novo nome do aluno escolhido anteriormente: ")
   l[a] = c
print(f"A lista de alunos desta classe ficou: {l}")