import funciones


def menu():
    print('''---------------------------------------------------------------
SISTEMA DE ADMINISTRACION DE CALIFICACIONES AED I
#1 CARGAR NOTA
#2 MOSTRAR TODAS LAS NOTAS
#3 ALUMNOS PROMOCIONADOS (PROMEDIO MAYOR O IGUAL A 7)
#4 PORCENTAJE DE REPROBADOS, REGULARES Y PROMOCIONADOS
#5 MEJORES PROMEDIOS
#0 FINALIZAR
---------------------------------------------------------------''')
    opcion = input("INGRESE UNA OPCION: ")
    return opcion


def menu_1():
    opcion = menu()
    calificaciones = {}
    while opcion != "0":
        if opcion == "1":
            alumno = input("Nombre del alumno: ")
            if alumno in calificaciones:
                calificaciones[alumno].extend(funciones.cargar_nota())
            else:
                calificaciones.update({alumno: funciones.cargar_nota()})
        if opcion == "2":
            funciones.mostrar_notas(calificaciones)
        if opcion == "3":
            funciones.promocionados(calificaciones)
        if opcion == "4":
            funciones.porcentaje(calificaciones)
        if opcion == "5":
            alumnos = {}
            import operator
            for key in calificaciones:
                promedio = sum(calificaciones.get(key)) / len(calificaciones.get(key))
                promedio_alumno = {key: promedio}
                alumnos.update(promedio_alumno)
            abanderados = sorted(alumnos.items(), key=operator.itemgetter(1), reverse=True)
            for i in abanderados[:3]:
                print(i)

        opcion = menu()


menu_1()
