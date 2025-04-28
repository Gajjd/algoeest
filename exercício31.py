def tabuada(numero):
    print(f"Tabada do {numero}:")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")


numero = int(input("Insira um número: "))
tabuada(numero)
