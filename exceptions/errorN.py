def get_at_content(dna):
    if dna.count("N") > 0:
        raise ValueError(f'Sequence contains {dna.count("N")} Ns')
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return at_content
print(get_at_content('ACGTACGTGAC'))
print(get_at_content('ACTGCTNAACT'))
