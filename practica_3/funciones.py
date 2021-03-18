'''
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
'''

lista = []
def funcion_1 ():
    monto = float(input('Monto abonado: '))
    lista.append(monto)

funcion_1()
