class Person:
    # Constructor
    def __init__(self, name="", age=0, dni=""):
        self.__name = name
        self.__age = age
        self.__dni = dni

    # Getters
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_dni(self):
        return self.__dni

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_dni(self, dni):
        self.__dni = dni

    # Metodos
    def mostrar(self):
        print(f"La persona creada se llama {self.get_name()}, tiene {self.get_age()} años de edad "
              f"y su numero de DNI es {self.get_dni()}.")

    def esmayordeedad(self):
        if self.__age >= 18:
            print("La persona es mayor de edad.")
        else:
            print("la persona es menor de edad.")


nombre = input("Nombre: ")
age_1 = 0
bucle = True
while bucle:
    age = input("Edad: ")
    if not age.isnumeric():
        print("Valor debe ser Int")
    else:
        age_1 = int(age)
        break
dni = input("DNI: ")

new_person = Person(nombre,age_1,dni)
new_person.mostrar()
new_person.esmayordeedad()
