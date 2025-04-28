def tabuada(base, inicio, fim):
    print(f"Tabada do {base} de {inicio} a {fim}:")
    for j in range(inicio, fim+1):
        print(f"{base} x {j} = {base*j}")


base = int(input("Insira um número: "))
inicio = int(input("Insira o número no qual sua tabuada vai começar: "))
fim = int(input("Insira o número no qual sua tabuada vai terminar: "))

tabuada(base, inicio, fim)