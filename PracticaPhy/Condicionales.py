def condicional():

    estudiante = input("Nombre: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    Definitiva = (nota1 + nota2 + nota3)/3
    if(Definitiva > 3.0):
        resultado = "aprobo"
    elif(Definitiva < 3.0):
        resultado = "desaprobo"

    print(f'        Notas del Estudiante        ')
    print(f'Primera nota: {nota1}')
    print(f'Segunda nota: {nota2}')
    print(f'Tercera nota: {nota3}')
    print(f'Resultado: {Definitiva}')
    print(f'El estudiante {resultado} la materia')

def universidad():
    VCarrera = int(input('Valor de la carrera a ingresar: '))
    Genero = input('Genero(Hombre/Mujer): ').upper()
    Edad = int(input('Ingrese su edad: '))
    Ciudad =  input('En que ciudad recide usted: ').upper()
    Hijos = input('Tiene hijos? (si/no): ').upper()

    if((Genero == 'MUJER' or Genero == 'HOMBRE') and Edad >= 18 and Ciudad == 'BELLO' and Hijos == 'NO'):
        beca = '100%'
        descuento = VCarrera * 0
    else:
        beca = '30%'
        descuento = VCarrera * 0.30

    print('         Programa de Becas de Bello          '.center(30))
    print(f'Costo de la carrera: {VCarrera}')
    print(f'Genero: {Genero}')
    print(f'Edad: {Edad}')
    print(f'Ciudad en la que recide: {Ciudad}')
    print(f'Tiene hijos?: {Hijos}')
    print(f'Ha ingresado sus datos correctamente, a usted se le dara una beca del {beca}, el total a pagar seria {descuento}')

def dias():
    dia = int(input('Que dia es hoy?'))
    if(dia >= 1 and dia <= 7):
        if(dia == 1):
            print('Lunes')
        elif(dia == 2):
            print('Martes')
        elif(dia == 3):
            print('miercoles')
        elif(dia == 4):
            print('Jueves')
        elif(dia == 5):
            print('Viernes')
        elif(dia == 6):
            print('Sabado')
        elif(dia == 7):
            print('Domingo')
    else:
        print('Dia incorrecto')

def notas():
    Estudiante = input('Nombre del estudiante: ')
    Nota1 = float(input('Nota1: '))
    Nota2 = float(input('Nota2: '))
    Nota3 = float(input('Nota3: '))
    Definitiva = (Nota1 + Nota2 + Nota3)/3

    if(Definitiva >= 0.1 and Definitiva <= 5.0):
        if(Definitiva >= 0.1 and Definitiva < 2.0):
            Resultado = 'Perdio por vago'
        elif(Definitiva >= 2.0 and Definitiva < 3.0):
            Resultado = 'Perdio pero puede recuperar'
        if(Definitiva >= 3.0 and Definitiva < 4.0):
            Resultado = 'Gano pero puede mejorar'
        if(Definitiva >= 4.0 and Definitiva < 4.6):
            Resultado = 'Sobresaliente'
        if(Definitiva >= 4.6 and Definitiva <= 5.0):
            Resultado = 'Eres Genial'

        print('         Notas Estudiante        '.center(30))
        print(f'Nombre del estudiante: {Estudiante}')
        print(f'Nota1: {Nota1}')
        print(f'Nota2: {Nota2}')
        print(f'Nota3: {Nota3}')
        print(f'Definitiva del Estudiante: {Definitiva}')
        print(f'El estudiante {Estudiante}, obtubo una definitiva de {Definitiva}, {Resultado}')

def gorda():
    estatura = float(input('Cual es su estatura? (en metros): '))
    peso = float(input('Cual es su peso? (en KG)'))
    IMC = peso / (estatura** 2)

    if(IMC < 18.5):
        salud = 'Bajo peso'
    if(IMC >= 18.5 and IMC < 25.0):
        salud = 'Peso saludable'
    if(IMC >= 25.0 and IMC < 30.0):
        salud = 'Sobrepeso'
    if(IMC >= 30.0 and IMC < 35.0):
        salud = 'Obesidad I'
    if(IMC >= 35.0 and IMC < 40.0):
        salud = 'Obesidad II'
    if(IMC >= 40.0):
        salud = 'Es mas facil saltarte que rodearte'

    print('         Salud       ')
    print(f'Estatura del paciente: {estatura}')
    print(f'Peso del paciente: {peso}')
    print(f'IMC del paciente: {IMC}')
    print(f'Resultado del IMC: {salud}')


#condicional()
#universidad()
#dias()
#notas()
#gorda()

