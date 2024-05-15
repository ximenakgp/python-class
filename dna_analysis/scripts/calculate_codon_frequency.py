"""
calculate_codon_frequency.py: Script para calcular la frecuencia de codones en una secuencia específica.

Este script lee una secuencia de ADN desde un archivo dado y calcula la frecuencia de cada codón
en esa secuencia. La secuencia de ADN debe estar en un archivo de texto y solo
contener los caracteres 'A', 'C', 'G', 'T', o 'N' (este último representa cualquier nucleótido). 
Opcionalmente, el cálculo puede normalizar el contenido excluyendo los caracteres 'N'.

Uso:
    python calculate_codon_frequency.py <path_to_dna_file> [--normalize]

Argumentos:
    <path_to_dna_file> : Ruta al archivo de texto que contiene la secuencia de ADN.
    --normalize        : Opción para normalizar el contenido de AT excluyendo 'N's del c
"""

import argparse
from dna_analysis.operations.codon_frequency import codon_frecuencia # Importa la funcion codon_frecuencia
from dna_analysis.utils.file_io import read_dna_sequence 

def main():
    parser = argparse.ArgumentParser(description="Calcula la frecuencia de codones en una secuencia de ADN")
    parser.add_argument("file", type=str, help="Archivo de ADN del cual leer la secuencia")

    args = parser.parse_args()
    file_path = args.file

    # Leer la secuencia del archivo 
    secuencia = read_dna_sequence(file_path)

    codones_frecuencia = codon_frecuencia(secuencia)

    # Imprimir las frecuencias de los codones
    for codon, frecuencia in codones_frecuencia.items():
        print('Codon:{}, Frecuencia:{:.2f}%'.format(codon, frecuencia))

if __name__ == "__main__":
    main()
