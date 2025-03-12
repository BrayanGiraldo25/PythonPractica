def intentos():
    intento = 3
    while(intento != 0):
        ingresar = print("Ingrese su usuario y Contraseña")
        usuario = input("Usuario: ").upper()
        passw = int(input("Contraseña: "))

        if(usuario != 'PACO' and passw != 123):
            intento -= 1
            print('Usuario y/o contraseña incorrecto')

        elif(usuario == "PACO" and passw == 123):
            print("Datos ingresados correctamente, bienvenido")
            break

        if(intento == 0):
            print("Eres un impostor, se bloqueara la cuenta")

intentos()

