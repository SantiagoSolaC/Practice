import funciones


def menu():
    print('''---------------------------------------------------------------\n
                        BIENVENIDO
    #1 INGRESAR UNA VENTA
    #2 MOSTRAR TODAS LAS VENTAS
    #3 MOSTRAR UNICAMENTE LA VENTA MAS BAJA
    #4 MOSTRAR LA GANANCIA TOTAL
    #5 CALCULAR EL PROMEDIO DE LAS VENTAS
    #0 PARA FINALIZAR\n
---------------------------------------------------------------\n''')

    opcion = input("Ingrese una opcion: ")
    return opcion


def menu_1():
    ventas = []
    opcion = menu()
    while opcion != "0":
        if opcion == "1":
            a = funciones.monto_venta()
            ventas.append(a)
        elif opcion == "2":
            funciones.mostrar_datos_lista(ventas)
        elif opcion == "3":
            print(f"La menor venta fue de: ${funciones.mostrar_venta_mas_baja(ventas)}")
        elif opcion == "4":
            print(f"La ganancia total es de: ${funciones.suma_total(ventas)}")
        elif opcion == "5":
            print(f"El promedio de las ventas es de: ${funciones.promedio_ventas_2(ventas)}")
        else:
            print("INGRESE UNA OPCION VALIDA!")
        opcion = menu()


menu_1()
