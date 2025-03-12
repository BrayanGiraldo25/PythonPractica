def print_h1(name):

    print(f'hola, {name}')

    print('Hola ' +  "Alumnos")

def factura():
    producto = input('Que producto compro?')
    cantidad = int(input('En cuanta cantidad?'))
    precio = int(input('Cual es el precio del producto?'))
    descuento = 0.10
    iva = 0.19
    subtotal = precio * cantidad
    vlrdescuento = subtotal * descuento
    vlriva = (subtotal-vlrdescuento)*iva
    netoPagar = subtotal - vlrdescuento + vlriva

    print('         Factura De Venta         ')
    print(f'Producto --> {producto}')
    print(f'Precio --> {precio}')
    print(f'Descuento --> {descuento}')
    print(f'Iva--> {iva}')
    print(f'Subtotal --> {subtotal}')
    print(f'Valor del Descuento --> {vlrdescuento}')
    print(f'Valor del Iva --> {vlriva}')
    print(f'Valor neto a pagar --> {netoPagar}')
    print(f'Muchas gracias por su compra')
    print(f'')


#factura()


def calificacion():
    estudiante = input('Nombre del estudiante: ')
    nota1 = float(input('Primera nota: '))
    nota2 = float(input('Segunda Nota: '))
    nota3 = float(input('Tercera Nota: '))
    definitiva = (nota1 + nota2 + nota3)/3

    print(f'        Calificaciones del estudiante       ')
    print(f'Nombre del Estudiante: {estudiante}')
    print(f'Primera Nota: {nota1}')
    print(f'Segunda Nota: {nota2}')
    print(f'Tercera Nota: {nota3}')
    print(f'Definitiva del Estudiante: {definitiva}')

#calificacion()
