import random
numero = random.randint(1,20)

palpite = 0
palpites = []
tentativas = 0

while palpite != numero:
    palpite = int(input("Dige um palpite entre 1 e 20: "))
    palpites.append (palpite)
    tentativas += 1

print(f"Parabéns, você acertou o número {numero} em {tentativas} tentativas, seus palpites foram:")
print(palpites)