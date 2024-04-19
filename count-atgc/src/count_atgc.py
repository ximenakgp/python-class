"""
PROGRAM NAME: 
Contenido de As, Ts, Gs, Cs
       
VERSION: 1.5

AUTHOR: KARLA XIMENA GONZALEZ PLATAS

DESCRIPTION: 
Programa que calcula el contenido de cada nucleótido en una secuencia de DNA. 
El usuario proporciona el nombre del archivo con la secuencia de DNA y el argumento para los nucleótidos que quiere contabilizar. 
Imprimir en pantalla el resultado de los conteos.
El programa considera excepciones y aplica la detección de posibles errores o bugs que pueden romper/detener la ejecución del programa.

CATEGORY:
    Conteo de nucleótidos en una secuencia de DNA/Python program

USAGE:
    % python count_atgc.py <file> -n A C T G
    % python count_atgc.py <file> -n a c t g
    % python count_atgc.py <file> -nucleotidos A C T G
    % python count_atgc.py <file> -nucleotidos a c t g

    
ARGUMENTS:
    POSICIONAL = archivo           => Nombre del archivo que contiene la secuencia de DNA que se quiere contabilizar
    OPCIONAL   = -n - -nucleotidos => Letras de los nucleótidos a contar (A,C, T, G ó a, c, t, g)

LIBRERÍA: 
    import argparse

METHOD:
-Importar la librería argparse para convertir el programa a uno de tipo CLI
-Crear el objeto ArgumentParser y añadir una descripción del programa
-Pasar los argumentos de acuerdo a lo que el usuario ingresa a la línea de comandos.
-Parsear los argumentos.
-Utilizar el bloque try y except para manejar los errores como excepciones.
-Abrir y cerrar el archivo que contiene la secuencia de DNA.
-Leer el contenido del archivo y almacenarlo en secuencia.
-1°Excepción: Verificar si la secuencia está vacía o no es válida.
-2°Excepción: Cuando el archivo no existe imprimir el error que se genera.
-Usar else para el caso en el que no ocurra ninguna excepción.
-Convertir la secuencia de DNA a mayúsculas para hacer el conteo sin distinción, es decir, sin 
importar si la secuencia de DNA tiene mayúsculas u minúsculas. 
-Imprimir un mensaje cuando exista un caracter no válido en la secuencia.
-Contar la frecuencia de los nucleótidos especificados en la línea de comandos.
-Hacer válido el argumento nucleotidos cuando el usuario lo ingresa en minúsculas
-Imprimir los resultados.
-Cerrar con una sentencia finally. 
"""
# ===========================================================================
# =                            main
# ===========================================================================

import argparse # Importar la líbreria de argparse

# Crear el objeto ArgumentParser y añadir una descripción del programa
parser = argparse.ArgumentParser(description='Programa para contar el contenido de nucleótidos en una secuencia de DNA :)')

# Pasar los argumentos
parser.add_argument("archivo", help="Introduce el nombre del archivo con la secuencia de DNA")
parser.add_argument("-n", "--nucleotidos", type=str, nargs="+", default=["A","C","T","G"], help="Letras de las que se desea ver la frecuencia")

# Parsear los argumentos
args = parser.parse_args()
archivo = args.archivo
nucleotidos = args.nucleotidos

# Abrir y cerrar el archivo que contiene la secuencia de DNA
try:
    with open(archivo, 'r') as file: # r se utiliza para abrir el archivo en modo lectura
        # Leer el contenido del archivo y almacenarlo en secuencia
        # strip borra espacios al inicio y al final de la cadena
        secuencia = file.read().strip()
        if not secuencia: # Verificar si el archivo esta vacio
            raise Exception("sorry, the file is empty") # Se genera una excepcion
except FileNotFoundError as ex:
    print("sorry, couldn't find the file:", archivo)
    print("ERROR:", ex.strerror) # Imprime el error que se genera

except Exception as ex: # Imprime el mensaje en la linea de comando
    print(ex)

else: # Si no hay ninguna excepcion se va a ejecutar lo siguiente

# Contar la frecuencia de los nucleótidos especificados en la línea de comandos
    # Convertir la secuencia a mayúsculas para llevar a cabo el conteo
    secuencia = secuencia.upper()
    if args.nucleotidos:
        for nucleotido in args.nucleotidos:
            # Hacer válido el argumento nucleotidos cuando el usuario lo ingresa en minúsculas
            nucleotido = nucleotido.upper()
            if nucleotido not in ["A","C","T","G"]: # Cuando existe un caracter no valido en la secuencia
                print(f"Sequence contains '{nucleotido}', it is invalid character")
            else:
                count = secuencia.count(nucleotido)
                print(f'Número de {nucleotido}: {count}')
    else:
        count_A = secuencia.count('A')
        count_C = secuencia.count('C')
        count_G = secuencia.count('G')
        count_T = secuencia.count('T')
        # Imprimir la frecuencia de los nucleótidos
        print(f'Número de A: {count_A}')
        print(f'Número de C: {count_C}')
        print(f'Número de G: {count_G}')
        print(f'Número de T: {count_T}')
finally: # Se ejecuta al final
    print(":)")
