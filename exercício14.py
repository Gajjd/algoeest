usuario = input("Insira o seu nome de usuário: ")
senha = input("Insira sua senha: ")
acesso = True
if usuario == "admin" and senha == "1234":
    print(f"Bem vindo, {usuario}")
else:
    acesso = False
    print(f"Usuário ou senha incorretos")