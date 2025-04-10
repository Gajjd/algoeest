numero = int(input("Insira um número para ver sua tabuada: "))
tabuada = []

for i in range(1,11):
    produto = numero * i
    tabuada.append (produto)

for i in range(1,11):
    print(f"{numero} x {i} = {tabuada[i-1]}")