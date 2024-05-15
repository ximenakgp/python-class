"""
codon_frequency.py: Módulo para calcular la frecuencias de codones en una secuencia de ADN.

Este módulo proporciona funciones para determinar la frecuencia de cada codón en una secuencia 
de DNA específica. 

Funciones:
- codon_frecuencia(secuencia): Devuelve la frecuencia de codones
"""

from collections import defaultdict  # Importa la clase defaultdict desde el módulo collections

def codon_frecuencia(secuencia):
    """
    Calcula la frecuencia de todos los codones en una secuencia de DNA

    Args:
        secuencia (str): secuencia de DNA a analizar
    
    Returns:
        codon_frecuencias: frecuencia de cada codón redondeada a 2 decimales
    
    Raises: 
        ValueError: Si la secuencia está vacía o contiene caracteres no válidos
    """
    # Validación básica de la secuencia
    if not secuencia:
        raise ValueError("La secuencia proporcionada está vacía.")
    
    secuencia = secuencia.upper()
    if any(c not in 'ACGUTN' for c in secuencia):
        raise ValueError("La secuencia contiene caracteres no válidos.")
    
    codon_count = defaultdict(int) # Crear un diccionario con valores enteros
    total_codons = 0 # Inicializar el contador 
    for i in range(0,len(secuencia), 3): # Iterar sobre la secuencia de 3 en 3 para obtener cada codon
        codon = secuencia[i:i+3] # Codon actual
        if len(codon) == 3:  # Asegurarse de que el codon tenga una longitud de 3 nucleotidos
            # Incrementar los contadores
            codon_count[codon] +=1 
            total_codons += 1
    codon_frecuencias = {codon: round((count / total_codons) * 100, 2) for codon, count in codon_count.items()} # Calcular la frecuencia de cada codon en porcentaje con 2 decimales
    return codon_frecuencias # Regresa la frecuencia de codones

if __name__ == "__main__":
# Bloques de prueba para demostrar la funcionalidad del módulo.
    # Declaracion de variable para prueba del modulo
    dna_sequence = "AUGATG"
    codon_frequencies = codon_frecuencia(dna_sequence)  # Calcula la frecuencia de cada codón en la secuencia de ADN

    # Imprimir las frecuencias de los codones
    for codon, frecuencia in codon_frequencies.items():
        print('Codon:{}, Frecuencia:{:.2f}%'.format(codon, frecuencia))
