# Funcion que comprueba si un valor puede ser float
def isfloat(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

# Creando clase
class Cuenta:
    # Constructor
    def __init__(self, titular="", cantidad=0.00):
        self.titular = titular
        self.cantidad = cantidad

    # Metodos
    def mostrar(self):
        print(f"El titular de la cuenta es {self.titular} y su contenido es de ${self.cantidad}.")
    
    def ingresar(self):
        bucle = True
        while bucle:
            ing = input(f"Ingrese el monto para sumar a la cuenta de {self.titular}: ")
            if isfloat(ing):
                ing = float(ing)
                if ing > 0.00:
                    self.cantidad = self.cantidad + ing
                    print(f"Ahora el saldo de la cuenta de {self.titular} es de ${self.cantidad}.")
                    break
                else:
                    print("El valor ingresado debe ser mayor a 0!")
            else:
                print("El valor ingresado debe ser numerico!")
    
    def retirar(self):
        bucle = True
        while bucle:
            ing = input(f"Ingrese el monto para restar a la cuenta de {self.titular}: ")
            if isfloat(ing):
                ing = float(ing)
                if ing > 0.00:
                    self.cantidad = self.cantidad - ing
                    print(f"Ahora el saldo de la cuenta de {self.titular} es de ${self.cantidad}.")
                    break
                else:
                    print("El valor ingresado debe ser mayor a 0!")
            else:
                print("El valor ingresado debe ser numerico!")

# Creando sub clase
class Cuenta_joven(Cuenta):
    # Constructor
    def __init__(self, titular="", cantidad=0.00, bonificacion=0, edad=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
        self.edad = edad

    # Metodos
    def estitularvalido(self):
        if 25 > self.edad >= 18:
            return True
        else:
            return False

    def retirar(self):
        if new_young_account.estitularvalido():
            bucle = True
            while bucle:
                ing = input(f"Ingrese el monto que se va a retirar de la cuenta de {self.titular}: ")
                if isfloat(ing):
                    ing = float(ing)
                    if ing > 0.00:
                        self.cantidad = self.cantidad - ing
                        print(f"Ahora el saldo de la cuenta de {self.titular} es de ${self.cantidad}.")
                        break
                    else:
                        print("El valor ingresado debe ser mayor a 0!")
                else:
                    print("El valor ingresado debe ser numerico!")        
        else:
            print("El titular no es valido para realizar un retiro de la cuenta!")

    def mostrar(self):
        print(f"El titular de la cuenta joven es {self.titular}, su contenido es de ${self.cantidad} y su bonificacion es de %{self.bonificacion}")

# Ingreso de datos
nombre = input("Ingrese nombre del titular de la cuenta: ")
monto = 0
bucle = True
while bucle:
    monto_1 = input("Ingrese el monto: ")
    if isfloat(monto_1):
        monto = float(monto_1)
        break
    else:
        print("El monto ingresado debe ser de tipo numerico!")

new_account = Cuenta(nombre, monto)
new_account.mostrar()
new_account.ingresar()
new_account.retirar()

nombre_joven = input("Ingrese nombre del titular de la cuenta joven: ")
edad_joven = 0
bucle = True
while bucle:
    edad_joven_1 = input("Ingrese la edad del titular de la cuenta joven: ")
    if not edad_joven_1.isnumeric():
        print("El valor ingresado debe ser numerico entero!")
    else:
        edad_joven = int(edad_joven_1)
        break
monto_joven = 0
bucle = True
while bucle:
    monto_1 = input("Ingrese el monto de la cuenta joven: ")
    if isfloat(monto_1):
        monto_joven = float(monto_1)
        break
    else:
        print("El monto ingresado debe ser de tipo numerico!")
bonificacion_joven = 0
bucle = True
while bucle:
    bonificacion = input("ingrese la bonificacion de la cuenta joven: ")
    if not bonificacion.isnumeric():
        print("El valor ingresado debe ser un numero entero!")
    else:
        bonificacion_joven = bonificacion
        break

new_young_account = Cuenta_joven(nombre_joven, monto_joven, bonificacion_joven, edad_joven)
new_young_account.retirar()
new_young_account.mostrar()
