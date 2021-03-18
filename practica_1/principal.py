from workspace.practica_1 import funciones


def menu():
    print("--------------------------------------------------------"
          "------\n"
          "BIENVENIDO!\n"
          "Ingrese 1 para verificar que un numero entero es mayor a 10.\n"
          "Ingrese 2 para verificar que la suma de dos valores es igual a un "
          "tercero.\n"
          "Ingrese 3 para ingresar 2 valor y calcular la division entre "
          "cuadrado del mayor y el cuadrado del menor.\n"
          "Ingrese 4 para calcular la temperatura en grados celcius a partir "
          "de la temperatura en grados fahrenheit.\n"
          "Ingrese 0 para finalizar.\n"
          "--------------------------------------------------------")
    opcion = input("Ingrese la opcion elegida: ")
    if opcion == "0":
        return
    elif opcion == "1":
        funciones.ej1()
    elif opcion == "2":
        par1 = float(input("Ingrese el primer valor: "))
        par2 = float(input("Ingrese el segundo valor: "))
        par3 = float(input("Ingrese el tercer valor: "))
        funciones.ej2(par1,par2,par3)
    elif opcion == "3":
        par1 = float(input("Ingrese el primer valor: "))
        par2 = float(input("Ingrese el segundo valor: "))
        print(funciones.ej3(par1, par2))
    elif opcion == "4":
        print(f"La temperatura es de {funciones.ej4()} grados celcius.")
    else:
        print("Ingrese una opcion valida!")
    menu()
menu()
