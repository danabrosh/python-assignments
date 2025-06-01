# Codon table 
codon_table = {
    'Phe': ['TTT', 'TTC'],
    'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile': ['ATT', 'ATC', 'ATA'],
    'Met': ['ATG'],
    'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr': ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr': ['TAT', 'TAC'],
    'His': ['CAT', 'CAC'],
    'Gln': ['CAA', 'CAG'],
    'Asn': ['AAT', 'AAC'],
    'Lys': ['AAA', 'AAG'],
    'Asp': ['GAT', 'GAC'],
    'Glu': ['GAA', 'GAG'],
    'Cys': ['TGT', 'TGC'],
    'Trp': ['TGG'],
    'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP': ['TAA', 'TAG', 'TGA']
}

codon_to_amino_acid = {}
for amino_acid, codons in codon_table.items():
    for codon in codons:
        codon_to_amino_acid[codon] = amino_acid

def count_amino_acids(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            # Handle FASTA format
            if content.startswith('>'):
                dna = ''.join(content.split('\n')[1:])
            else:
                dna = content
            dna = dna.strip().upper()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        dna = input("Please enter a DNA sequence:").strip().upper()

    counts = {}
    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i+3]
        if codon in codon_to_amino_acid:
            amino_acid = codon_to_amino_acid[codon] 
            if amino_acid not in counts:
                counts[amino_acid] = 0
            counts[amino_acid] += 1

    return counts

if __name__ == "__main__":
    result = count_amino_acids("dna_sequence.txt")
    
    if not result:
        print("There are no amino acids in the sequence.")
    else:
        print("\nAmino Acid Counts:")
        for amino_acid, count in sorted(result.items()):
            print(f"{amino_acid}: {count}")