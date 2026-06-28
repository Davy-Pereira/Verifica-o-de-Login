def login(func):
    def wrapper(user: str, password:str ) -> None:
        if user == "admin" and password == "123":
            func(user)
            print("Acesso Liberado")
        else:
            print("Acesso Negado")
    return wrapper

@login
def menu(user):
    print(f"Bem vindo {user}")

menu("admin", "123")