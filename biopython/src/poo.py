'''
NAME: 
    Programacion Orientada a Objetos: Creacion de superclase y clase
VERSION:
    1
    
AUTHOR: 
    Karla Ximena Gonzalez Platas

DESCRIPTION:
    El programa crea una superclase llamada animal, despues genera otras dos clases, perro y gato.
    Ambas clases van a hacer un override del metodo haz_ruido() con sus respectivos sonidos (guauguauu, miaumiaaauu).
    En la clase gato se agrega el atributo "usa_arenero". 
    Al final, se crean 2 objetos, un perro y un gato con los cuales se llaman a sus respectivas funciones y a 'dict'

CATEGORY:
        POO: Programacion Orientada a Objetos

USAGE:
        % python poo.py
    
ARGUMENTS:
    Nombre del programa:
        poo.py

METHOD:
    1. Se crea la clase perro y la clase gato, heredando la superclase animal
        1.1 Se crea el constructor
    2. Se sobreescribe la funcion haz_ruido() en la clase perro y gato para que cada uno haga el sonido correcto
    3. Se agrega el atributo "usa_arenero" para la clase gato
    4. Se crea un objeto gato y un objeto perro con sus respectivos atributos y se generan sus respectivos ruidos
    5. Se llama a 'dict' 

'''

class animal(): # Se crea la superclase animal
    
    def __init__(self, nombre, edad): # Creacion del constructor
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
    # Definir metodos
    def haz_ruido(self):
        return "AAAAAAAA"

class perro(animal): # Se crea una clase llamada perro 
    def haz_ruido(self): # Define el metodo haz_ruido en perro sobreescribiendo en animal
        return "guauguauu"

class gato(animal): # Se crea una clase llamada gato
    def __init__(self, nombre, edad, usa_arenero): # Define e inicializa el metodo
        super().__init__(nombre, edad) # inicializa nombre y edad
        self.usa_arenero = usa_arenero # se asigna usa_arenero al atributo del mismo nombre
    
    def haz_ruido(self):
        return "miaumiaaauu"

# Crear objetos perro y gato
Freya = perro(nombre="Freya", edad=7)
Senna = gato(nombre="Senna", edad=1, usa_arenero=True)

# Llamar a la función haz_ruido() y a __dict__
print(f"{Freya.nombre} hace: {Freya.haz_ruido()}")
print(f"Propiedades de Freya: {Freya.__dict__}")

print(f"{Senna.nombre} hace: {Senna.haz_ruido()}")
print(f"Propiedades de Senna: {Senna.__dict__}")



