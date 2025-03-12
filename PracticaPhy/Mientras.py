def mientras():
    while True:
        respuesta = int(input("¿De cuánto es el número? "))


        if respuesta >= 1 and respuesta <= 9:
            print("La respuesta es un número del 1 al 9")
        else:
            print("La respuesta no es lo esperado")
            break


if __name__ == "__main__":
    mientras()