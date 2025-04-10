palavras = []
palindromos = []

for i in range (1,6):
    palavra = input(f"Insira a {i}° palavra: ")
    palavras.append (palavra)
    
for palavra in palavras:
    if palavra ==palavra[::-1]:
        palindromos.append (palavra)
    
print("Palavras que são palíndromo:")
for palindromo in palindromos:
    print(palindromo)