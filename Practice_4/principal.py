import funciones

def menu():
    print('''---------------------------------------------------------------
                    BIENVENIDO
    #1 CREAR UNA CUENTA
    #2 LISTAR TODAS LAS CUENTAS
    #3 LISTAR TODAS LAS CUENTAS CON SALDO MAYOR A $1000
    #4 SUMATORIA DE TODAS LAS CUENTAS
    #5 COMISIONES
    #6 CONSULTAR LOS 5 CLIENTES MAS IMPORTANTES
    #0 FINALIZAR
---------------------------------------------------------------''')
    opcion = input("SELECCIONE UNA OPCION: ")
    return opcion


def menu_1():
    opcion = menu()
    lista_cuentas = []
    while opcion != "0":
        if opcion == "1":
            a = funciones.cargar_cuenta()
            lista_cuentas.append(a)
        elif opcion == "2":
            funciones.listado_cuentas(lista_cuentas)
        elif opcion == "3":
            funciones.mayor_1000(lista_cuentas)
        elif opcion == "4":
            funciones.sumatoria_total(lista_cuentas)
        elif opcion == "5":
            comi = funciones.comisiones()
            for cuentas in lista_cuentas:
                print(cuentas * comi)
        elif opcion == "6":
            funciones.mejores_clientes()
        else:
            print("INGRESE UNA OPCION VALIDA")
        opcion = menu()


menu_1()
