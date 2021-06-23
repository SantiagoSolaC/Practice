def cargar_nota():
    lista_nota = []
    bucle = True
    while bucle == True:
        nota = int(input("Ingrese nota o 0 para continuar: "))
        if 1 <= nota <= 10:
            lista_nota.append(nota)
        else:
            break
    return lista_nota


def mostrar_notas(calificaciones):
    for a, n in calificaciones.items():
        print(a, n)


def promocionados(calificaciones):
    for key in calificaciones:
        promedio = sum(calificaciones.get(key))/len(calificaciones.get(key))
        if promedio >= 7:
            print(key, f"- Promedio: {promedio}")
        else:
            continue


def porcentaje(calificaciones):
    promos = []
    regulares = []
    reprobados = []
    for key in calificaciones:
        promedio = sum(calificaciones.get(key))/len(calificaciones.get(key))
        if promedio >= 7:
            promos.append(1)
        if 7 > promedio >= 4:
            regulares.append(1)
        if promedio < 4:
            reprobados.append(1)
        else:
            continue
    print(f"Promocionados: {int(sum(promos) / len(calificaciones.keys()) * 100)}%\n"
          f"Regulares: {int(sum(regulares) / len(calificaciones.keys()) * 100)}%\n"
          f"Reprobados: {int(sum(reprobados) / len(calificaciones.keys()) * 100)}%")
