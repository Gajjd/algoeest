numeros = []
soma = 0

for i in range(1,11):
    numero = float(input(f"Insira o {i}° número: "))
    numeros.append(numero)

print(numeros)

for numero in numeros:
    soma += numero

print(f"a soma dos números {numeros} é {soma}")