# Módulo at_content

Fecha: 14/05/2024

**Participantes / Autor**: 

- Karla Ximena González Platas <ximenagp@lcg.unam.mx>

## Descripción del Problema
Este módulo proporciona funciones para determinar el porcentaje de las bases de adenina (A)
y timina (T) en una secuencia de ADN dada. Esto es útil para estudios genéticos donde
las proporciones de AT pueden ser indicativas de ciertas características genómicas.

## Especificación de Requisitos

Requisitos funcionales

- Calcula el contenido porcentual de adenina (A) y timina (T) en una secuencia de ADN.
- Se valida la secuencia de DNA 
- Normaliza sin contar las N
- El usuario debe proporcionar el archivo con la secuencia de DNA

Requisitos no funcionales
- Módulo realizado en python.
- Ejecución y tiempo de respuesta rápido.

## Análisis y Diseño    

Calcula el contenido de A y T en una secuencia de DNA  

Pseudocogido simple que ilustre la logica basica del script:

```
def calculate_at_content(sequence, normalize=True):
    """
    Calcula el contenido porcentual de adenina (A) y timina (T) en una secuencia de ADN.

    Args:
        sequence (str): La secuencia de ADN a analizar.
        normalize (bool): Si True, normaliza el contenido de AT en caso de que haya 'N's en la secuencia.

    Returns:
        float: El porcentaje de contenido de AT en la secuencia.

    Raises:
        ValueError: Si la secuencia está vacía o contiene caracteres no válidos.
    """

    # Validación básica de la secuencia
    if not sequence:
        raise ValueError("La secuencia proporcionada está vacía.")
    
    sequence = sequence.upper()
    if any(c not in 'ACGTN' for c in sequence):
        raise ValueError("La secuencia contiene caracteres no válidos.")

    a_count = sequence.count('A')
    t_count = sequence.count('T')
    at_count = a_count + t_count

    if normalize: #Normaliza sin contar las ns
        total_count = sequence.count('A') + sequence.count('C') + sequence.count('G') + sequence.count('T')
        if total_count == 0:
            return 0
        return (at_count / total_count) * 100
    else:
        total_length = len(sequence)
        return (at_count / total_length) * 100

if __name__ == "__main__":
    # Prueba de funcionalidad.
    # Esto es mas manual y el assert es mas automatico 
    test_sequence = "ACTGNAT"
    print(f"Contenido de AT en la secuencia de prueba: {calculate_at_content(test_sequence, normalize=True)}%")
```

El formato de los datos de entrada: .txt

#### Caso de uso: Módulo para contar el contenido de As y Ts en una secuencia de ADN
```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada
                 v
         +-----------------+
         |                 |
         |  Calcula el     |
         |   contenido     |
         |    de A y T     |
         |                 |
         +-----------------+
```

- **Actor**: Usuario

- **Descripción**: El actor proporciona un archivo de entrada

- **Flujo principal**:
    - El módulo contiene la función calculate_at_content que calcula el contenido de A y T
    - El módulo se importa desde un programa llamado calculate_at_content.py
	
- **Flujos alternativos**:
	- La función del módulo considera las siguientes excepciones:
        - Cuando:
            - La secuencia proporcionada está vacía
            - La secuencia contiene caracteres no válidos
        - Además normaliza el conteo sin considerar las Ns
    
