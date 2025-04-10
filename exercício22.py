palavras = []
palavra_com_mais_de_5_letras = 0
palavras_com_mais_de_5_letras = []

for i in range (1,7):
    palavra = input(f"Insira a {i}° palavra: ")
    palavras.append (palavra)

for palavra in palavras:
    if len(palavra) >= 5:
        palavra_com_mais_de_5_letras += 1
        palavras_com_mais_de_5_letras.append (palavra)

print(f"Das palavras {palavras}, {palavra_com_mais_de_5_letras} têm mais de cinco letras. Elas são as {palavras_com_mais_de_5_letras}")
