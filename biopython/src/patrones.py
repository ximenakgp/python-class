# Importar
from Bio import SeqUtils
from Bio.Seq import Seq
# Patron a buscar
pattern = Seq("ACG")
# Secuencia en donde buscaremos el patron
sequence = Seq("ATGCGCGACGGCGTGATCAGCTTATAGCCGTACGACTGCTGC")
# El resultado de la busqueda lo guarda en una variable
result = SeqUtils.nt_search(str(sequence), pattern)
print(result)

consensus = "RGWYV"
sequence = "CGTAGCTAGCTCAGAGCAGGGACACGTGCTAGCAACAGCGCT"
results = SeqUtils.nt_search(sequence,consensus) # Busca una secuencia manejando el alfabeto IUPAC
print(results)

# parsea archivo example.fasta, puedes obtener id, seq, name, features, etc..
for record in SeqIO.parse("ejemplo.fasta", "fasta"):
    print(record.id)
# alternativamente se puede usar lo siguiente    
with open("ejemplo.fasta") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        print(record.id)