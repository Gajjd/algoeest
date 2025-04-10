notas = []
soma = 0

for i in range (1,6):
    nota = float(input(f"Nota do {i}° aluno: "))
    notas.append (nota)

for nota in notas:
    soma += nota

media = soma / len(notas)

print(f"A média das notas {notas} é: {media}")