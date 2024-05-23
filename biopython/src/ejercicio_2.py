from Bio import SeqIO
# parsea archivo example.fasta, puedes obtener id, seq, name, features, etc..
for record in SeqIO.parse("ejemplo.fasta", "fasta"):
    print(record.id)
# alternativamente se puede usar lo siguiente    
with open("ejemplo.fasta") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        print(record.id)

record = SeqIO.read("single.fasta", "fasta")