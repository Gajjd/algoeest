usuario = input("Insira o seu nome de usuário: ")
senha = input("Insira sua senha: ")

acesso = False

if usuario == "admin" and senha == "1234":
    acesso = True
    print(f"Bem vindo, {usuario}")
else:
    print(f"Usuário ou senha incorretos")

#  # Facilitar para outros programas
# print(f"Acesso: {acesso}")
