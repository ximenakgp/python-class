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



