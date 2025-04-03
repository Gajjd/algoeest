nota1 = float(input("1° nota: "))
nota2 = float(input("2° nota: "))
nota3 = float(input("3° nota: "))
media = (nota1 + nota2 + nota3) / 3
aprovado = False
recuperacao = False
if media >=7:
    aprovado = True
    print("Aprovado")
elif media <7 and media >=5:
    recuperacao = True 
    print("Recuperação")
else:
    print("Reprovado")