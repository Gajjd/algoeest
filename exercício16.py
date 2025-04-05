nota1 = float(input("1° nota: "))
nota2 = float(input("2° nota: "))
nota3 = float(input("3° nota: "))

media = (nota1 + nota2 + nota3) / 3

aprovado = False
recuperacao = False
reprovado = False

if media >= 7:
    aprovado = True
    print("Aprovado")
elif 7 > media >= 5:
    recuperacao = True
    print("Recuperação")
else:
    reprovado = True
    print("Reprovado")

#  #Essa parte seria mais para caso a escola quisesse ter a tomada de decisão automático
# print(f"Aprovado: {aprovado}")
# print(f"Recuperação: {recuperacao}")
# print(f"Reprovado: {reprovado}")
