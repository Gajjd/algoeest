nome = input("Nome: ")
idade = int(input("Idade: "))
turma = input("Turma: ")
matricula = True
if idade >= 6:
    print(f"Aluno cadastrado com sucesso: {nome}, {idade} anos, turma {turma}")
else:
    matricula = False
    print("Matrícula negada")