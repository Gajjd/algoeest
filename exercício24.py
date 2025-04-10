numeros = []
maior = 0

for i in range(1,6):
    numero = int(input(f"Insira o {i}° número: "))
    numeros.append (numero)
    menor = numero

for numero in numeros:
    if maior < numero:
        maior = numero
    if menor > numero:
        menor = numero

print(f"Na lista {numeros}, o maior número é {maior} e o menor número é {menor}")




