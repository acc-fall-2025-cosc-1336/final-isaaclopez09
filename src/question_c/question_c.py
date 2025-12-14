#write functions here, don't add input('') statements here!
def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    len_s = len(dna_string1)
    len_t = len(dna_string2)
    for i in range(len_s - len_t + 1):
        if dna_string1[i:i + len_t] == dna_string2:
            positions.append(i +1)
    return tuple(positions)

    