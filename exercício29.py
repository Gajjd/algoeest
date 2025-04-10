valores = []
valores_multiplicados = []

for i in range(1,5):
    valor = int(input(f"Insira o {i}° valor: "))
    valores.append (valor)

multiplicador = int(input("Insira o multiplicador: "))

for valor in valores:
    valor_multiplicado = valor * multiplicador
    valores_multiplicados.append (valor_multiplicado)

print(f"Os valores {valores} multiplicados por {multiplicador} viraram:")
print(valores_multiplicados)