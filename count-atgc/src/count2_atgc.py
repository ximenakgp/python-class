"""
NAME: 
Contenido de As, Ts, Gs, Cs
       
VERSION: 1

AUTHOR: 
KARLA XIMENA GONZALEZ PLATAS

DESCRIPTION: 
Programa que calcula el contenido de cada nucleótido en una secuencia de DNA. 
La secuencia viene en un archivo de texto en formato raw llamado sequence.txt. 
Imprimir en pantalla el resultado de los conteos.

CATEGORY:
    Conteo de nucleótidos en una secuencia de DNA/Python program

USAGE:
    % python count2_atgc.py
    
ARGUMENTS:
    Archivo: "sequence.txt" => Contiene la secuencia de DNA que se quiere contabilizar. 

METHOD:
-Crear o nombrar un archivo como "sequence.txt" que contenga la secuencia de DNA.
-Abrir el archivo con la secuencia de DNA
-Convertir la secuencia de DNA a mayúsculas para hacer el conteo sin distinción, es decir, sin 
importar si la secuencia de DNA tiene mayúsculas u minúsculas. 
-Inicializar contadores para cada nucleótido.
-Contar el numero de nucleotidos.
-Imprimir los resultados.
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
    with open(archivo, 'r') as file:
        # Leer el contenido del archivo y almacenarlo en secuencia
        secuencia = file.read().strip()
except FileNotFoundError as e:
    print("El archivo especificado no se encontró")
    print(e)
    exit(1)
# Verificar si la secuencia está vacía o no es válida
if not secuencia:
    print("El archivo está vacío o no contiene una secuencia de ADN válida")
    exit(1)

# Convertir la secuencia a mayúsculas para llevar a cabo el conteo
secuencia = secuencia.upper()

# Contar la frecuencia de los nucleótidos especificados en la línea de comandos
if args.nucleotidos:
    for nucleotido in args.nucleotidos:
        # Hacer válido el argumento nucleotidos cuando el usuario lo ingresa en minúsculas
        nucleotido = nucleotido.upper()
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