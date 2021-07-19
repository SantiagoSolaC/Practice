def cargar_cuenta():
    saldo = int(input("Ingrese monto a depositar: "))
    return saldo


def listado_cuentas(lista_cuentas):
    for i in lista_cuentas:
        print(i)


def mayor_1000(lista_cuentas):
    for index, saldo in enumerate(lista_cuentas):
        if saldo >= 1000:
            print(index, saldo)


def sumatoria_total(lista_cuentas):
    print(sum(lista_cuentas))

    """
    Ó
    sumatoria = 0
    largo = len(lista_cuentas)
    for i in range(0, largo):
        sumatoria = sumatoria + lista_cuentas[i]
    print(sumatoria)
    """


def comisiones():
    c = int(input("Ingrese el porcentaje de comision a aplicar: "))
    return c / 100


def mejores_clientes():
    lista_mejores = []
    for i in range(0, 5):
        mejores = input("Ingrese un nombre: ")
        lista_mejores.append(mejores)
    print(lista_mejores)
