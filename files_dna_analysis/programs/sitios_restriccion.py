"""
Programa para identificar sitios de restricción en una secuencia de ADN.

Uso:
    python sitios_restriccion.py archivo_adn.txt

Argumentos:
    archivo_adn.txt: Nombre del archivo que contiene la secuencia de ADN.

Descripción:
    Este programa lee una secuencia de ADN desde un archivo y busca los sitios de restricción
    para un conjunto de enzimas de restricción definidas en el programa. Los resultados,
    que incluyen las posiciones de los sitios de corte y las enzimas correspondientes,
    se imprimirán en la salida estándar.

Requerimientos:
    La secuencia de ADN debe estar en formato de texto plano y contener solo caracteres
    válidos ('A', 'C', 'G', 'T').
"""

import argparse

# Diccionario que mapea enzimas de restricción a sus secuencias de reconocimiento
ENZIMAS_RESTRICCION = {
    "EcoRI": "GAATTC",
    "BamHI": "GGATCC",
    "HindIII": "AAGCTT"
}

def read_dna_sequence(filename):
    """
    Lee la secuencia de ADN de un archivo.

    Args:
        filename (str): Nombre del archivo.

    Returns:
        str: Secuencia de ADN.
        
    Raises:
        AssertionError: Si la secuencia contiene caracteres no válidos.
    """
    with open(filename, 'r') as file:
        sequence = file.read().strip().upper()
    assert all(c in 'ACGT' for c in sequence), "La secuencia contiene caracteres no válidos."
    return sequence

def find_restriction_sites(dna, enzymes):
    """
    Busca los sitios de restricción en la secuencia de ADN para las enzimas dadas.

    Args:
        dna (str): Secuencia de ADN.
        enzymes (dict): Diccionario de enzimas y sus secuencias de reconocimiento.

    Returns:
        dict: Diccionario de sitios de restricción con enzimas como claves y listas de posiciones como valores.
    """
    sites = {enzyme: [] for enzyme in enzymes}
    for enzyme, recognition_seq in enzymes.items():
        pos = dna.find(recognition_seq)
        while pos != -1:
            sites[enzyme].append(pos)
            pos = dna.find(recognition_seq, pos + 1)
    return sites

def main():
    parser = argparse.ArgumentParser(description="Identifica sitios de restricción en una secuencia de ADN.")
    parser.add_argument("file", type=str, help="Archivo de ADN a procesar")
    args = parser.parse_args()

    try:
        dna_sequence = read_dna_sequence(args.file)
        restriction_sites = find_restriction_sites(dna_sequence, ENZIMAS_RESTRICCION)
        
        print("Sitios de restricción encontrados:")
        for enzyme, positions in restriction_sites.items():
            positions_str = ', '.join(str(pos) for pos in positions)
            print(f"{enzyme}: Posiciones -> {positions_str}")

    except FileNotFoundError:
        print(f"Error: El archivo '{args.file}' no se encontró.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()