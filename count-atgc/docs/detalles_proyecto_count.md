# COUNT A, C, G Y T

Fecha:19/04/24

**Participantes / Autor**:

- Karla Ximena González Platas  <ximenagp@lcg.unam.mx>

## Descripción del Problema
El proyecto consiste en crear un programa en python, para contar las ocurrencias de los símbolos A, C, G y T de una secuencia de DNA que se lee a través de un archivo proporcionado por el usuario, sin importar si existen mayúsculas o minúsculas dentro de la secuencia. Por lo tanto, al final de la ejecución del programa se imprime la cantidad de As, Cs, Ts, y Gs que se encuentran en la cadena de DNA. El programa considera excepciones y aplica la detección de posibles errores o bugs que pueden detener la ejecución del programa; para ello se hace uso del bloque try y except, las excepciones consideran cuando el archivo esta vacío o no existe. De la misma manera, en caso de que el usuario ingrese un cáracter no válido para el argumento nucleótido, el programa imprime cual es este cáracter y genera un mensaje de advertencia. 

## Especificación de Requisitos

### Requisitos funcionales

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

### Requisitos no funcionales

- Programa realizado en python.
- Programa de tipo CLI
- Ejecución y tiempo de respuesta rápido.
- El usuario debe proporcionar dos argumentos: el archivo de entrada y los nucleótidos a contar.
- Manejo de excepciones


## Análisis y Diseño

Para crear este programa, se usaron diferentes comandos y variables de Python, además se consideraron diferentes excepciones para validar los datos del archivo. A continuación, se muestra un pseudocódigo simple para ilustrar la lógica básica del script:

```
import argparse 

parser = argparse.ArgumentParser(description='Programa para contar el contenido de nucleótidos en una secuencia de DNA :)')

parser.add_argument("archivo", help="Introduce el nombre del archivo con la secuencia de DNA")
parser.add_argument("-n", "--nucleotidos", type=str, nargs="+", default=["A","C","T","G"], help="Letras de las que se desea ver la frecuencia")

args = parser.parse_args()
archivo = args.archivo
nucleotidos = args.nucleotidos

try:
    with open(archivo, 'r') as file: 
        secuencia = file.read().strip()
        if not secuencia: 
            raise Exception("sorry, the file is empty") 
except FileNotFoundError as ex:
    print("sorry, couldn't find the file:", archivo)
    print("ERROR:", ex.strerror) 

except Exception as ex: 
    print(ex)

else: 
    secuencia = secuencia.upper()
    if args.nucleotidos:
        for nucleotido in args.nucleotidos:
            nucleotido = nucleotido.upper()
            if nucleotido not in ["A","C","T","G"]: 
                print(f"Sequence contains '{nucleotido}', it is invalid character")
            else:
                count = secuencia.count(nucleotido)
                print(f'Número de {nucleotido}: {count}')
    else:
        count_A = secuencia.count('A')
        count_C = secuencia.count('C')
        count_G = secuencia.count('G')
        count_T = secuencia.count('T')
        
        print(f'Número de A: {count_A}')
        print(f'Número de C: {count_C}')
        print(f'Número de G: {count_G}')
        print(f'Número de T: {count_T}')
finally: 
    print(":)")

```

Los datos de entrada son dos argumentos que debe proporcionar el usuario en la línea de comandos, el primero es el nombre del archivo con la secuencia de DNA y el otro son los nucleótidos que se quieren contabilizar. Este archivo debe contener la secuencia de DNA, tanto en mayúsculas como en minúsculas. En caso de que no se cumpla con los parametros especificados el programa maneja excepciones y valida los datos del archivo

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

- **Descripción**: El usuario proporciona un archivo de entrada con la secuencia de DNA y ingresa las letras de los nucleótidos que quiere contabilizar. El sistema ejecuta el programa y calcula la cantidad de nucleótidos en la secuencia de DNA.

- **Flujo principal**:
        1. El usuario proporciona el archivo de entrada con la secuencia de DNA.
        3. El usuario ingresa como argumento las letras de los nucleótidos a contabilizar.
	2. El sistema valida el archivo y los datos de entrada.
	3. El sistema calcula la cantidad de As, Gs, Cs y Ts.
	4. El sistema imprime el resultado.

	
- **Flujos alternativos**:
        - Si el usuario no ingresa las letras de los nucleótidos a contar.
                3. El programa contabiliza todos los nucleótidos de la secuencia de DNA.
        - Si el usuario ingresa un caracter invalido para el argumento nucleótido 
                4. El programa imprime un mensaje de advertencia 
        - Si el usuario ingresa todas las letras mayúsculas o minúsculas en el argumento nucleotidos
                5. El programa se ejecuta correctamente
        Excepciones:
	    - Si el archivo proporcionado no tiene el nombre correcto
		        1. El sistema proporciona un mensaje diciendole al usuario que el archivo no se encontró.
        - Si el archivo proporcionado esta vacío 
                2. El sistema manda un mensaje al usuario diciendole que el archivo esta vacío.


