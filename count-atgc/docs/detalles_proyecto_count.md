# COUNT A, C, G Y T

Fecha:21/03/24

**Participantes / Autor**:

- Karla Ximena González Platas  <ximenagp@lcg.unam.mx>

## Descripción del Problema
El proyecto consiste en crear un programa en python, para contar las ocurrencias de los símbolos A, C, G y T de una secuencia de DNA que se lee a través de un archivo nombrado como "sequence.txt" sin importar si existen mayúsculas o minúsculas dentro de la secuencia. Por lo tanto, al final de la ejecución del programa se imprime la cantidad de As, Cs, Ts, y Gs que se encuentran en la cadena de DNA. 

## Especificación de Requisitos

Requisitos funcionales

- Crear o nombrar un archivo como "sequence.txt" que contenga la secuencia de DNA.
- Abrir el archivo con la secuencia de DNA.
- Convertir la secuencia de DNA a mayúsculas para hacer el conteo sin distinción, es decir, sin 
  importar si la secuencia de DNA tiene mayúsculas u minúsculas. 
- Inicializar contadores para cada nucleótido.
- Contar el número de nucleótidos.
- Imprimir los resultados.

Requisitos no funcionales

- Programa realizado en python.
- Ejecución y tiempo de respuesta rápido.
- El archivo de entrada debe ser nombrado como "sequence.txt".


## Análisis y Diseño

Para crear este programa, se usaron diferentes comandos y variables de Python, además se consideraron diferentes excepciones para validar los datos del archivo. A continuación, se muestra un pseudocódigo simple para ilustrar la lógica básica del script:

```
with open('sequence.txt', 'r') as file:
    sequence = file.read().strip()


sequence = sequence.upper()


count_A = sequence.count('A')
count_C = sequence.count('C')
count_G = sequence.count('G')
count_T = sequence.count('T')


print(f'Número de A: {count_A}')
print(f'Número de C: {count_C}')
print(f'Número de G: {count_G}')
print(f'Número de T: {count_T}')

```

El formato de los datos de entrada es .txt y el nombre completo del archivo es: "sequence.txt". Este archivo debe contener la secuencia de DNA, tanto en mayúsculas como en minúsculas.

#### Caso de uso: Conteo de As, Ts, Gs, Cs

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada
                 v
         +-----------------+
         |                 |
         |  Conteo de As,  |
         |   Ts, Gs, Cs    |
         |                 |
         +-----------------+
```

- **Actor**: Usuario

- **Descripción**: El usuario proporciona un archivo de entrada con la secuencia de DNA. El sistema ejecuta el programa y calcula la cantidad de nucleótidos en la secuencia de DNA.

- **Flujo principal**:
        1. El usuario crea/proporciona el archivo de entrada con la secuencia de DNA.
	2. El sistema valida el archivo y los datos de entrada.
	3. El sistema calcula la cantidad de As, Gs, Cs y Ts.
	4. El sistema imprime el resultado.

	
- **Flujos alternativos**:
	- Si el archivo proporcionado no tiene el nombre correcto
		1. El sistema no ejecuta el programa.

