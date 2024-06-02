'''
NAME: 
    Trabajando con un archivo FASTA
    
VERSION:
    1
    
AUTHOR: 
    Karla Ximena Gonzalez Platas

DESCRIPTION:

El programa procesa un archivo en formato FASTA llamado 'seq.nt.fa' que contiene secuencias de ADN. 
Para cada secuencia en el archivo, se extraen los codones en los seis marcos de lectura (tres en 
direccion directa y tres en direccion inversa) y se escriben los resultados en archivos FASTA separados 
para cada marco y direccion de lectura, el nombre de estos archivos lleva esta estructura: 
seq_1_Frame_1_Directa.fasta

El proceso de calculo de codones se realiza mediante una funcion que se llama seis veces para cada 
secuencia del archivo, una vez por cada marco de lectura.
    
CATEGORY:
        Biopython: Secuencias y Formatos

USAGE:
        % python fasta.py
    
METHOD:

El codigo utiliza la biblioteca Biopython para manipular secuencias de ADN y archivos en formato FASTA. 
Se definen varias funciones que realizan tareas especificas como extraer codones, crear registros de 
secuencia, escribir en archivos FASTA y procesar secuencias en diferentes marcos de lectura y en dos 
direcciones (directa y reversa).
El programa principal lee el archivo FASTA especificado 'seq.nt.fa' y procesa cada secuencia en los seis 
marcos de lectura y direcciones, guardando los resultados en el directorio 'results/'.
    
'''
# ===========================================================================
# =                            Imports
# ===========================================================================

# Importacion de biblioteca y modulos
from Bio import SeqIO # Modulo para escribir y leer secuencias
from Bio.Seq import Seq # Modulo para crear secuencias
from Bio.SeqRecord import SeqRecord # Modulo para crear registros de secuencias con metadatos

# ===========================================================================
# =                            Functions
# ===========================================================================


def extraer_codones(secuencia, marco):
    """
    Extrae los codones de una secuencia de ADN en un marco de lectura especifico y los devuelve separados por espacio.

    Parametros:
        secuencia (str): La secuencia de ADN de la cual se extraen los codones.
        marco (int): El marco de lectura en el cual se extraen los codones.

    Return:
        str: Una cadena donde los codones estan separados por espacio.
    """
    # Lista de comprension para extraer codones de la secuencia en el marco dado
    codones = [secuencia[i:i+3] for i in range(marco, len(secuencia), 3) if len(secuencia[i:i+3]) == 3]
    return ' '.join(codones)  # Une los codones separados por espacio en una sola cadena


def crear_registro_secuencia(id_sec, codones, marco, es_reversa):
    """
    Crea un registro de secuencia a partir de codones y con metadatos como ID y descripcion.

    Parametros:
        id_sec (str): El identificador unico de la secuencia.
        codones (list): Una lista de codones que componen la secuencia.
        marco (int): El marco de lectura en el cual se leyeron los codones.
        es_reversa (bool): Indica si la secuencia se lee en direccion reversa.

    Return:
        SeqRecord: registro de secuencia con la informacion proporcionada.

    """
    if es_reversa:
        direccion = "Reversa"
    else:
        direccion = "Directa"
    descripcion = f"{id_sec} Marco {marco+1} {direccion}" # Crea una descripcion para el SeqRecord
    secuencia = Seq(''.join(codones))  # Convierte la lista de codones en una secuencia de cadena unica usando la clase seq
    return SeqRecord(secuencia, id=id_sec, description=descripcion)

def escribir_codones_en_fasta(registro_secuencia, nombre_archivo_salida):
    """
    Escribe un registro de secuencia en un archivo en formato FASTA.

    Parametros:
        registro_secuencia (SeqRecord): El registro de secuencia a escribir en el archivo.
        nombre_archivo_salida (str): El nombre del archivo de salida donde se escribira el registro.

    """
    with open(nombre_archivo_salida, 'w') as archivo_salida:
        SeqIO.write(registro_secuencia, archivo_salida, "fasta")

def procesar_secuencia(id_sec, secuencia, directorio_salida=""):
    """
    Procesa una secuencia de ADN en los tres marcos de lectura y escribe los resultados en archivos FASTA.

    Parametros:
        id_sec (str): El identificador unico de la secuencia.
        secuencia (str): La secuencia de ADN que se va a procesar.
        directorio_salida (str, opcional): El directorio donde se guardaran los archivos FASTA resultantes. Por defecto es el directorio actual.
    """
    # Procesa la secuencia en los tres marcos de lectura
    for marco in range(3): # Itera sobre los tres marcos de lectura
        # Procesa la secuencia en direccion directa
        codones_d = extraer_codones(secuencia, marco)
        registro_sec_d = crear_registro_secuencia(id_sec, codones_d, marco, False)
        file_d = f"{directorio_salida}{id_sec}_Frame{marco+1}_Directa.fasta" # Crea el nombre del archivo de salida para la secuencia en direccion directa
        escribir_codones_en_fasta(registro_sec_d, file_d)
        
        # Procesa la secuencia en direccion inversa
        sec_complement_r = str(Seq(secuencia).reverse_complement())
        codones_r = extraer_codones(sec_complement_r, marco)
        registro_sec_r = crear_registro_secuencia(id_sec, codones_r, marco, True)
        file_r = f"{directorio_salida}{id_sec}_Frame{marco+1}_Reversa.fasta"
        escribir_codones_en_fasta(registro_sec_r, file_r)

# ===========================================================================
# =                            Main
# ===========================================================================

def principal():

    nombre_archivo_entrada = 'seq.nt.fa'  # Especifica el nombre del archivo FASTA que se va a procesar
    directorio_salida = 'results/'  # Directorio de salida deseado
    secuencias = SeqIO.to_dict(SeqIO.parse(nombre_archivo_entrada, "fasta")) # Lee el archivo FASTA y convierte el generador de secuencias en un diccionario.
    
    for id_sec, registro in secuencias.items(): # Itera sobre cada secuencia en el archivo
        secuencia = str(registro.seq) # Convierte la secuencia del SeqRecord en una cadena de texto
        procesar_secuencia(id_sec, secuencia, directorio_salida) # Procesa la secuencia en todos los marcos de lectura.
if __name__ == "__main__":
    principal()
