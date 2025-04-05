idade = int(input("Digite a idade do público: "))
genero = input("Digite o gênero do público (masculino/feminino): ").lower()

if idade < 15:
    print("Artigo infantil")
    
elif 15 <= idade <= 21 and genero == "feminino":
    print("Maquiagem e moda")
    
elif 15 <= idade <= 32 and genero == "masculino":
    print("Artigo esportivo")
else:
    print("Nenhum artigo disponível para esse público.")
