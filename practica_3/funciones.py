"""
Una librería de la ciudad de Carlos Paz requiere de un programa que permita
cargar los montos de todas las ventas realizadas en el mes. Para ello el
programa debe permitir guardar ese valor en una lista.
Se debe generar un menú que permita realizar las siguientes operaciones:

Agregar el monto de una venta.
Mostrar todos los datos en la lista.
Mostrar la venta más baja.
Mostrar la ganancia total (Suma de todas las ventas).
Calcular el promedio de Ventas.

Cada opción debe llamar a una función que se encargue de hacer el calculo
correspondiente recibiendo la lista por parametro y retornando el valor
correspondiente.
"""


def monto_venta():
    monto = float(input('Monto abonado: '))
    return monto


def mostrar_datos_lista(ventas):
    lis = len(ventas)
    for i in range(0, lis):
        dato = ventas[i]
        print(dato)


def mostrar_venta_mas_baja(ventas):
    x = ventas[0]
    for i in ventas:
        if i < x:
            x = i
    return x


"""
    Ó
    minimo = min(lista)
    print(minimo)
    Ó
    return min(lista)
    """


def suma_total(ventas):
    ganancia = 0
    largo_lista = len(ventas)
    for i in range(0, largo_lista):
        ganancia = ganancia + ventas[i]
    return ganancia


def promedio_ventas(ventas):
    cant_venta = 0
    suma_venta = 0
    prom_ventas = 0
    ven = len(ventas)
    for i in range(0, ven):
        suma_venta = suma_venta + ventas[i]
        cant_venta = cant_venta + 1
        prom_ventas = suma_venta / cant_venta
    return prom_ventas


def promedio_ventas_2(ventas):
    prom_ventas = suma_total(ventas) / len(ventas)
    return prom_ventas

