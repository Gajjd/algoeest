#isso é um comentário.

# print ("mensagem")
# # print é op mesmo que escreval (ele printa para o usuario)


# idade= 6
# altura= 0.50
# peso= 5.950
# nome = "francisco"
# print (idade, altura, peso, nome)
# # a variavel recebe com =


# nome=input("insira nome")
# # o INPUT le o que o usuario escrever em forma de texto (string)
# idade= int(input("insira idade"))
# # o INT(INPUT) le o que o usuario escrever em forma de numero inteiro (intire)
# peso= float(input("inaira seu peso"))
# # o FLOAT(INPUT) le o que o usuario escrever em forma de numero real (float)
# print (f"{nome} {idade} anos {peso} kg") 
# # f tem função de formatação, ele junta valores de variaveis com textos


# pedaco_pizza = 5
# cliente="john"
# print(type(pedaco_pizza))
# print(type(cliente))
# # O TYPE faz o programa entender o tipo do texto (string, int, float...)


# pedaco_pizza=input("Informe quantos pedaços comeu")
# print(type(pedaco_pizza))
# # Esse TYPE leu como str (texto) pois colocamos input ao inves de int(input)


# a=4
# A="Sally"
# print(a)
# print(A)
# # O python diferencia variaveis maiusculas e minusculas


# fruta1,fruta2,fruta3="Laranja","Banana","Maça"
# print(fruta1,fruta2,fruta3)
# #Podemos declarar e printar variaveis na mesma linha, dividindo-as por,


# num1=5
# num2=9
# print(num1+num2)


# nome=input("qual o vingador mais forte?")
# print(f"Olá,{nome}!")
# if nome == "hulk":
#     print ("Bem-vindo vingador mais forte!")
# else:
#     print("acesso negado")
# #Precisa estar alinhado para o python entender que está no mesmo comando
# # Trocamos o entao pelo : (Também e necessario usar o : depois do else)


# x= int(input("Insira um número"))
# if x>2 and x<10:
#     print(f"O número {x} está entre 2 e 10")
# else:
#     print(f"O número {x} não está entre 2 e 10")
# # o AND precisa que as duas condiçoes sejam verdadeiras


# x=3
# if x<2 or x>4:
#     print ("O número é menor que 2 ou maior que 4")
# # o OR só precisa que uma condição seja verdadeira


# x=5 
# if not x > 10:
#     print("O número não é maior que 10.")
#     #O NOT inverte o valor da condiçao (verdadeiro=falso e falso=verdadeiro),logo o x não é maior que 10.


# x=5
# y=2
# if x>2 and (y>10 or not x ==5):
#     print("Condição atendida")
# else: 
#     print("Condição não atendida")
# # Podemos juntar as condições, fazendo uma condição ficar complexa
# # A ordem na qual o phyton avalia os operadores é not, and, or