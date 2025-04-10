nomes =  []

for i in range(1,6):
    nome = input(f"Insira o {i}° nome: ")
    nomes.append (nome)

nomes.sort()

print(f"Nomes em ordem alfabética: {nomes}")