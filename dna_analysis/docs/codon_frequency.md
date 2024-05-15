# Módulo codon_frequency

Fecha: 14/05/2024

**Participantes / Autor**:

- Karla Ximena González Platas  <ximenagp@lcg.unam.mx>

## Descripción del Problema
El módulo contiene la función "codon_frecuencia" para calcular la frecuencia de todos los codones que se encuentran en una secuencia de DNA. 

## Especificación de Requisitos

Requisitos funcionales

- Calcular la frecuencia de codones 
- El usuario debe proporcionar el archivo con la secuencia 

Requisitos no funcionales

- Módulo realizado en python.
- Ejecución y tiempo de respuesta rápido.

## Análisis y Diseño    

Módulo para calcular la frecuencias de codones en una secuencia de ADN.

pseudocogido simple que ilustre la logica basica del script:
```
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
    dna_sequence = "AUGAAAGGTGUGAATATGATGATGATGATGATG"
    codon_frequencies = codon_frecuencia(dna_sequence)  # Calcula la frecuencia de cada codón en la secuencia de ADN

```

El formato de los datos de entrada.

#### Caso de uso: Calcular la frecuencia de todos los codones

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada
                 v
         +-----------------+
         |                 |
         |   Calcula la    |
         |   frecuencia    |
         |   de codones    |
         +-----------------+
```

- **Actor**: Usuario

- **Descripción**: El actor proporciona un archivo de entrada-Que hace el programa
- **Flujo principal**:
- Se importa la clase defaultdict desde el módulo collections para crear un diccionario
- Calcula la frecuencia de cada codón en porcentaje con 2 decimales

- **Flujos alternativos**:
	- Casos especiales en el programa:
        - La función asegura que el codón que se está contando tiene una longitud de 3 nucleótidos
        - Se consideran excepciones: 
            - Cuando la secuencia está vacía o contiene caracteres inválidos
