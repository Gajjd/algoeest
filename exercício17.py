ano_nascimento = int(input("Digite o ano que nasceu: "))
ano_atual = int(input("Digite o ano atual: "))

if ano_nascimento > ano_atual:
    print("Ano de nascimento não pode ser maior que o ano atual. Tente novamente.")
else:
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        print(f"Maior de idade. Você tem {idade} anos.")
    else:
        print(f"Menor de idade. Você tem {idade} anos.")
