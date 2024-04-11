# Casos de prueba o escenarios

Este documento describe los casos de prueba para el script de Python desarrollado para contar la frecuencia de nucleótidos de una secuencia de DNA ubicada en un archivo que el usuario ingresa a la línea de comandos. El objetivo de estas pruebas es validar y garantizar que el script funciona correctamente y cumple con las especificaciones.

Los casos de prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script así como los posibles errores que puedan surgir.

El script está diseñado para contar las ocurrencias de los símbolos A, C, G y T de una secuencia de DNA que se lee a través de un archivo proporcionado por el usuario en la línea de comandos; de modo que el programa recibe dos argumentos: el primero de ellos es el nombre del archivo y el segundo los nucleótidos específicos que se quieren contar de la secuencia, sin importar si existen mayúsculas o minúsculas dentro de esta. Por lo tanto, al final de la ejecución del programa se imprime la cantidad de As, Cs, Ts, y Gs que se encuentran en la cadena de DNA.

Además, el script está diseñado para manejar errores, uno de estos, es cuando el usuario pasa como argumento un nombre incorrecto del archivo que contiene la secuencia o cuando el archivo con la secuencia del DNA esta vacía. Así como también cuando el usuario no ingresa ningún argumento para nucleótidos, por lo que se ponen valores por default y se calculan las frecuencias de todos los nucleótidos o cuando el argumento que ingresan son letras minúsculas, es decir a, c, t o g. 

Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y fiabilidad del script.

La ejecución exitosa de estos casos de prueba asegura que el script está listo para su uso y puede manejar diferentes condiciones de entrada y situaciones de error.

A continuación, presentamos los detalles de los casos de prueba. Cada caso de prueba incluye una descripción del caso de prueba, los datos de entrada utilizados y el resultado esperado.
    
    
### Caso de prueba 1: Validación input del usuario

- Descripción: Para este caso, se le proporcionará al usuario un path incorrecto de un archivo inexistente, para observar si el programa puede manejarlo apropiadamente
- Datos de entrada:
```{python}
python count-atcg the_file_does_not_exist.txt -n ACGT
```
- Resultado esperado: ---
- Estado: -----

### Caso de prueba 2: Comprobación de error ----

- Descripción: Verificar que el script puede ------
- Datos de entrada: ---
- Resultado esperado: ---
- Estado: ----

### Caso de prueba 1: Comprobación de ----

- Descripción: Verificar que el script puede ----
- Datos de entrada: ----
- Resultado esperado: ---
- Estado: -----

### Caso de prueba 1: Comprobación de ----

- Descripción: Verificar que el script puede ----
- Datos de entrada: ----
- Resultado esperado: ---
- Estado: -----
