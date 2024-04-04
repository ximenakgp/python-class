"""
NAME:Contenido de As, Ts, Gs, Cs
       
VERSION:1

AUTHOR: KARLA XIMENA GONZALEZ PLATAS

DESCRIPTION: Programa que calcula el contenido de cada nucleótido en una secuencia de DNA. 
La secuencia viene en un archivo de texto en formato raw llamado sequence.txt. Imprimir en pantalla el resultado de los conteos.

CATEGORY
    
USAGE

    % python count_atgc.py
    
ARGUMENTS

METHOD

"""

# Abrir el archivo con la secuencia de ADN
with open('sequence.txt', 'r') as file:
    sequence = file.read().strip()

# Convertir la secuencia a mayúsculas para contar sin distinción de mayúsculas y minúsculas
sequence = sequence.upper()

# Inicializar contadores
count_A = sequence.count('A')
count_C = sequence.count('C')
count_G = sequence.count('G')
count_T = sequence.count('T')

# Imprimir los resultados
print(f'Número de A: {count_A}')
print(f'Número de C: {count_C}')
print(f'Número de G: {count_G}')
print(f'Número de T: {count_T}')