# COUNT As, Cs, Gs Y Ts

El proyecto consiste en crear un programa en Python que cuenta las ocurrencias de los nucleótidos A, C, G y T en una secuencia de DNA proporcionada por el usuario a través de un archivo. Este programa de tipo CLI permite ingresar los nucleótidos a contar como argumentos en la línea de comandos y cuenta los nucleótidos sin importar si están en mayúsculas o minúsculas en la secuencia. Al finalizar la ejecución, el programa imprime la cantidad de As, Cs, Ts y Gs encontrados en la cadena de DNA. 
Por otro lado, el programa considera excepciones y aplica la detección de posibles errores o bugs que pueden detener la ejecución; para ello se hace uso del bloque try y except, las excepciones consideran cuando el archivo esta vacío o no existe. De la misma manera, en caso de que el usuario ingrese un cáracter no válido para el argumento nucleotidos, el programa imprime cual es este cáracter y genera un mensaje de advertencia. 


## Uso

Usted puede usar este script de la siguiente manera:
El script acepta dos argumentos, el nombre del archivo con la secuencia de DNA y los nucleótidos a contar:

```
python count_atgc.py <archivo> -n A T C G
python count_atgc.py <archivo> -nucleotidos A T C G
python count_atgc.py <archivo> -n a c t g
python count_atgc.py <archivo> -nucleotidos a c t g
python count_atgc.py <archivo>

```

Donde 'archivo' es el nombre del archivo que contiene la secuencia de DNA. El archivo debe contener las letras A, C, T, G (en mayúsculas ó minúsculas), debido a que estas representan los nucleótidos.

## Salida

El script imprimirá la cantidad de As, Cs, Gs o Ts en la consola. 

## Control de errores

Si el archivo proporcionado no existe, el script generará un mensaje de error.
Si el archivo proporcionado contiene una secuencia vacía, el programa imprime un mensaje de error.
Si el usuario no ingresa las letras de los nucleótidos, el programa contabiliza todos por default.
Si el usuario ingresa un carácter inválido para el argumento nucleótidos, se imprime un mensaje de error. 

## Pruebas

El script incluye un conjunto de pruebas unitarias. Puede ejecutar estas pruebas con:

```
python count_atgc.py <archivo> -n A T C G
python count_atgc.py <archivo> -nucleotidos a c t g

python count_atgc.py <nombre incorrecto del archivo> -nucleotidos a c t g

python count_atgc.py <archivo> -n A T C G
python count_atgc.py <archivo> -nucleotidos A T C G

python count_atgc.py <archivo vacío> -n 

python count_atgc.py <archivo>

python count_atgc.py <archivo> -n N K Y

```


## Datos
El script está diseñado para operar en un archivo de texto plano, con una secuencia de letras. No hay restricciones en el número de letras en el archivo.

## Metadatos y documentación
Este README ofrece información de uso básico. 

## Código fuente
El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Términos de uso

Este script está disponible bajo la licencia [MIT License]. Consulte el archivo LICENSE para obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite: [https://github.com/ximenakgp/python-class].

## Contáctenos

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotros en: [ximenagp@lcg.unam.mx].
