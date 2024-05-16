import Bio.Seq
seqobj = Bio.Seq.Seq('ATGCGATCGAGC')
seqobj
print(seqobj)
seq_str = str(seqobj)
print('{} tiene {} nucleotidos'.format(seq_str, len(seq_str)))

#seqobj es inmutable

seq_str = seq_str[::-1]#nos da un valor de inicio y un valor final al usar menos 1 es el tamaño del paso
print(seq_str)
# Secuencia complementaria
c= seqobj.complement()
print(c)
# Secuencia reversa
r= seqobj.reverse_complement()
print(r)
# Traduccion a proteina
p= seqobj.translate(to_stop = True)
print(p)

# Obtener transcripto
rna = seqobj.transcribe()
print(rna)

# retrotranscripto
rna_t=rna.back_transcribe()
print(rna_t)

