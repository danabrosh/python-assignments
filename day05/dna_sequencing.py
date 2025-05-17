import sys

def find_dna_sequences(sequence):
    # Split the sequence at X and filter empty strings
    seq_X = sequence.split("X")
    seq_list = []
    
    # Add non-empty sequences that only contain ACTG
    for seq in seq_X:
        if seq and all(base in 'ACTG' for base in seq):
            seq_list.append(seq)
    
    # Sort by length in descending order
    return sorted(seq_list, key=len, reverse=True)


sequence = sys.argv[1]
result = find_dna_sequences(sequence)
print(result)
