# Casos de prueba o escenarios

Este documento describe los casos de prueba para el script de Python desarrollado para contar la frecuencia de nucleótidos de una secuencia de DNA ubicada en un archivo que el usuario ingresa a la línea de comandos. El objetivo de estas pruebas es validar y garantizar que el script funciona correctamente y cumple con las especificaciones.

Los casos de prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script así como los posibles errores que puedan surgir.

El script está diseñado para contar las ocurrencias de los símbolos A, C, G y T de una secuencia de DNA que se lee a través de un archivo proporcionado por el usuario en la línea de comandos; de modo que el programa recibe dos argumentos: el primero de ellos es el nombre del archivo y el segundo los nucleótidos específicos que se quieren contar de la secuencia, sin importar si existen mayúsculas o minúsculas dentro de esta. Por lo tanto, al final de la ejecución del programa se imprime la cantidad de As, Cs, Ts, y Gs que se encuentran en la cadena de DNA.

Además, el script está diseñado para manejar errores, uno de estos, es cuando el usuario pasa como argumento un nombre incorrecto del archivo que contiene la secuencia o cuando el archivo con la secuencia del DNA esta vacía. Así como también cuando el usuario no ingresa ningún argumento para nucleótidos, por lo que se ponen valores por default y se calculan las frecuencias de todos los nucleótidos o cuando el argumento que ingresan son letras minúsculas, es decir a, c, t o g. 

Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y fiabilidad del script.

La ejecución exitosa de estos casos de prueba asegura que el script está listo para su uso y puede manejar diferentes condiciones de entrada y situaciones de error.

A continuación, presentamos los detalles de los casos de prueba. Cada caso de prueba incluye una descripción del caso de prueba, los datos de entrada utilizados y el resultado esperado.
    
    
### Caso de prueba 1: Comprobación de paso de argumentos a la línea de comandos

- Descripción: Verificar que el script puede contar los nucleótidos que se encuentran en un archivo con la secuencia de DNA 
- Datos de entrada: Nombre del archivo con la secuencia y argumento de los nucleotidos a buscar
- Resultado esperado: 
Número de A: 48
Número de C: 28
Número de T: 48
Número de G: 32
- Estado: Correcto

### Caso de prueba 2: Comprobación de error cuando el usuario pasa el archivo con un nombre incorrecto

- Descripción: Verificar que el script puede detectar un error cuando el usuario pasa como argumento un nombre incorrecto del archivo que contiene la secuencia
- Datos de entrada: Nombre incorrecto del archivo con la secuencia y argumento de los nucleotidos a buscar
- Resultado esperado: El archivo especificado no se encontró
- Estado: Correcto

### Caso de prueba 3: Comprobación de paso de argumentos que representan los nucleótidos tanto en mayúsculas como minúsculas. 

- Descripción: Verificar que el script puede reconocer como argumento válido las letras A, C, T, G y a, c, t, g.
- Datos de entrada: Nombre del archivo y argumento para los nucleótidos
- Resultado esperado: 
Número de A: 48
Número de C: 28
Número de T: 48
Número de G: 32
- Estado: Correcto

### Caso de prueba 4: Comprobación de detección de error cuando el archivo con la secuencia esta vacío

- Descripción: Verificar que el script puede detectar si existe una secuencia en el archivo proporcionado por el usuario. 
- Datos de entrada: Nombre del archivo y argumento para los nucleótidos
- Resultado esperado: El archivo está vacío o no contiene una secuencia de ADN válida
- Estado: Correcto

### Caso de prueba 5: Comprobación de valores default cuando el usuario no ingresa argumentos para los nucleotidos
- Descripción: Verificar que el script puede colocar valores por default cuando el usuario no ingresa los nucleótidos que quiere contar. 
- Datos de entrada: Nombre del archivo 
- Resultado esperado: 
Número de A: 48
Número de C: 28
Número de T: 48
Número de G: 32
- Estado: Correcto
