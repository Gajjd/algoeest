numeros = []
par = []
impar = []

for i in range(1,9):
    numero = int(input(f"Insira o {i}° número: "))
    numeros.append (numero)

for numero in numeros:
    if numero % 2 == 0:
        par.append (numero)
    else:
        impar.append (numero)

print(f"Na lista {numeros},")
print(f"os pares são: {par} e os ímpares são: {impar}")