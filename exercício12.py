saldo = int(input("Insira o saldo dessa conta."))

acesso = True

if saldo >0 :
    print("Conta ativa.")
else :
    acesso = False
    print("Conta desativada.")

#   # Facilitar para outros programas
# print(f"acesso: {acesso}")
