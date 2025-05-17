
def find_dna_sequences(sequence):
    # First split by all non-ACTG characters
    seq_list = []
    current = ""
    
    for char in sequence:
        if char in 'ACTG':
            current += char
        else:
            if current:
                seq_list.append(current)
                current = ""
    
    # Don't forget the last sequence
    if current:
        seq_list.append(current)
    
    # Sort by length in descending order
    return sorted(seq_list, key=len, reverse=True)

print("Please type in a sequence:")
sequence = input()
result = find_dna_sequences(sequence)
print(result)

