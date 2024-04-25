"""
Programa para calcular el contenido de AT de una secuencia de ADN.

Uso:
    python contenido_at.py archivo_adn.txt

Argumentos:
    archivo_adn.txt: Nombre del archivo que contiene la secuencia de ADN.

Descripción:
    Este programa lee la secuencia de ADN desde un archivo y calcula el contenido de AT (adenina y timina)
    en la secuencia. Los resultados se imprimirán en la salida estándar.
    La secuencia de ADN debe contener solamente caracteres válidos ('A', 'C', 'G', 'T').
"""

import argparse

def read_dna_sequence(filename):
    """
    Lee la secuencia de ADN de un archivo.

    Args:
        filename (str): Nombre del archivo.

    Returns:
        str: Secuencia de ADN.
        
    Raises:
        AssertionError: Si la secuencia contiene caracteres no válidos o está vacía.
    """
    with open(filename, 'r') as file:
        sequence = file.read().strip().upper()
    assert all(c in 'ACGT' for c in sequence), "La secuencia contiene caracteres no válidos."
    return sequence

def calculate_at_content(sequence):
    """
    Calcula el porcentaje de contenido de AT en una secuencia de ADN.

    Args:
        sequence (str): Secuencia de ADN.
        
    Returns:
        float: Porcentaje de contenido de AT.
    """
    at_count = sequence.count('A') + sequence.count('T')
    at_content = (at_count / len(sequence)) * 100
    return at_content

def main():
    parser = argparse.ArgumentParser(description="Calcula el contenido de AT de una secuencia de ADN.")
    parser.add_argument("file", type=str, help="Archivo de ADN a procesar")
    args = parser.parse_args()
    
    try:
        dna_sequence = read_dna_sequence(args.file)
        at_percentage = calculate_at_content(dna_sequence)
        print(f"El contenido de AT en la secuencia es: {at_percentage:.2f}%")
    except FileNotFoundError:
        print(f"Error: El archivo '{args.file}' no se encontró.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()