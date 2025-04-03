ano_nascimento = int(input("Digite o ano que nasceu: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nascimento
if idade >=18:
    print(f"Maior de idade. você tem {idade} anos.")
else:
    print(f"Menor de idade. você tem {idade} anos.")