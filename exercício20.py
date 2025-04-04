idade = int(input("Idade: "))
membro = input("Membro (sim/não/acompanhado): ").lower()
acesso = False
if idade >=18:
    if membro == "sim":
        acesso = True
        print("Liberado")
    elif membro == "não":
        pago = input("Pague o valor completo. Pagou? (sim/não): ").lower()
        if pago == "sim":
            acesso = True
            print("Liberado")
        else:
            print("Recusado")
    elif membro == "acompanhado":
        pago = input("Pague metade do valor. Pagou (sim/não): ").lower()
        if pago == "sim":
            acesso = True
            print("Liberado")
        else:
            print("Recusado")
    else:
        print("Recusado")
else:
    print("Recusado")