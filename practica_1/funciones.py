"""
- Método sin retorno y sin parámetros que permita escribir un algoritmo que
lea un número entero y verifique si es mayor a 10. Si lo es escribir el número
 y si no lo es escribir un mensaje que diga que el número es menor o igual
"""


def ej1():
    a = int(input("--------------------------\n"
                  "Ingrese un numero entero: "))
    if a > 10:
        print(f"El numero {a} es mayor a 10.")
    else:
        print("--------------------------------------------\n"
              "El numero que ingreso es menor o igual a 10.")


"""
- Metodo sin retorno  con parámetros que reciba 3 números, y determine si la 
suma del primero y el segundo es igual al tercero. Si se cumple, escribir "La 
suma es igual al tercero", si no, escribir "La suma es distinta al tercero".
"""


def ej2(a, b, c):
    if c == a+b:
        print("----------------------------\n"
              "la suma es igual al tercero.")

    else:
        print("-------------------------------\n"
              "la suma es distinta al tercero.")


"""
- Método con retorno y con parámetros que cuando recibe dos número enteros,
 calcule el resultado de dividir el cuadrado del mayor de ellos y el cuadrado
  del menor de ellos. Si los números son iguales retornar el número 1
"""


def ej3(a, b):
    c = a**2/b**2
    d = b**2/a**2
    if a > b:
        return c
    elif a < b:
        return d
    else:
        return 1


"""
- Método con retorno y sin parámetros que convierta temperaturas de 
Fahrenheit a Celcius. Utilizar la fórmula ºC = (5/9)·(ºF – 32).
"""


def ej4():
    tempf = float(input("---------------------------------------------\n"
                        "Ingrese la temperatura en grados Fahrenheit: "))
    tempc = (5/9)*(tempf-32)
    return tempc
