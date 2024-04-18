def get_at_content(dna):
    if dna.count("N") > 0:
        raise ValueError(f'Sequence contains {dna.count("N")} N\'s')
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return at_content

sequences = ['ACGTACGTGAC', 'ACTGCTNAACT', 'ATGGCGCTAGC']
for seq in sequences:
    try:
        print('AT content for ' + seq + ' is ' + str(get_at_content(seq)))
    except ValueError as ex:
        print('skipping invalid sequence '+ ex.args[0])
