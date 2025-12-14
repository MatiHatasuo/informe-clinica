from controllers.auth import login

def menu_principal():
    print("=== MediPlus ===")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    tipo = login(usuario, clave)

    if tipo:
        print("Sesión iniciada como", tipo)
    else:
        print("Credenciales incorrectas")
