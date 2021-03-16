"""
Nombre de la función: ejercicio_1_for_en_vector En esta función agregar el
vector: nombres = [‘Lucas’,’Franco’,’Luciano’,’Malena’,’Jonatan’,’Luciano’,
’Rodrigo’,’Maria Sol’,’Enzo’,’Milena’]
Recorra el vector e imprima los elementos utilizando el ciclo for sin índices
(sin la función range)
"""
def ejercicio_1_for_en_vector ():
    nombres = ['Lucas','Franco','Luciano','Malena','Jonatan','Luciano',
               'Rodrigo','Maria Sol','Enzo','Milena']
    for n in (nombres):
        print(n)

"""
Nombre de la función: ejercicio_2_for_en_vector En esta función agregar el 
vector: nombres = [‘Lucas’,’Franco’,’Luciano’,’Malena’,’Jonatan’,’Luciano’,
’Rodrigo’,’Maria Sol’,’Enzo’,’Milena’]
Recorra el vector e imprima los elementos utilizando el ciclo for e indicando 
en qué índice (posición del vector) se encuentra cada elemento.
"""
#Alternativa 1 de hacerlo
def ejercicio_2_for_en_vector_1 ():
    nombres = ['Lucas','Franco','Luciano','Malena','Jonatan','Luciano',
               'Rodrigo','Maria Sol','Enzo','Milena']
    nom = len(nombres)
    for i in range (0,nom):
        print(f'#{i} {nombres[i]}')
#Alternativa 2 de hacerlo
def ejercicio_2_for_en_vector_2 ():
    nombres = ['Lucas', 'Franco', 'Luciano', 'Malena', 'Jonatan', 'Luciano',
               'Rodrigo', 'Maria Sol', 'Enzo', 'Milena']
    for index, l in enumerate(nombres):
        print(index, l)

"""
Nombre de la función: ejercicio_3_for_en_vector En esta función agregar el 
vector: nombres = [‘Lucas’,’Franco’,’Luciano’,’Malena’,’Jonatan’,’Luciano’,
’Rodrigo’,’Maria Sol’,’Enzo’,’milena’]

Recorra el vector a partir del elemento número 5 e imprima los elementos 
restantes. Además mostrar el valor en la posición 1

Resultado esperado: ’Jonatan’,’Luciano’,’Rodrigo’,’Maria Sol’,’Enzo’,’Milena’
Elemento en posición 1: Franco
"""
def ejercicio_3_for_en_vector ():
    nombres = ['Lucas','Franco','Luciano','Malena','Jonatan','Luciano',
               'Rodrigo','Maria Sol','Enzo','Milena']
    nom = len(nombres)
    for i in range(4,nom):
        print(nombres[i])
    print(f'El elemento en posicion 1: {nombres[1]}')

"""
Nombre de la función: ejercicio_4_while Realice una funcion que mientras la 
nota ingresada sea distinta de 0 le solicite al profesor el ingreso de otra 
nota, una vez que el profesor ingrese la nota 0 deberá imprimir un mensaje 
con el promedio de todas las notas ingresadas.
"""
def ejercicio_4_while ():
    nota = 1
    cant_nota = 0
    nota_acum = 0
    while nota != 0:
        nota = float(input("Ingrese una nota: "))
        if nota != 0:
            nota_acum = nota_acum + nota
            cant_nota += 1
    prom = nota_acum / cant_nota
    return prom
    print(f'El promedio de las notas ingresadas es {ejercicio_4_while()}')

ejercicio_2_for_en_vector_2()