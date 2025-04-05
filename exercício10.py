valor = float(input("Insira o valor da compra"))

descont10 = valor-valor*0.1
descont20 = valor-valor*0.2
descont25 = valor-valor*0.25

if valor<100:
    print(f"Total: R${valor}")

elif valor >=100 and valor <500:
    print(f"Total: R${descont10}")

elif valor >=500 and valor<1000:
    print(f"Total: R${descont20}")

else:
    print(f"Total: R${descont25}")
