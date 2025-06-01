def get_codon_table():
    return {
        'Phe': ['TTT', 'TTC'], 'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
        'Ile': ['ATT', 'ATC', 'ATA'], 'Met': ['ATG'], 'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
        'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], 'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
        'Thr': ['ACT', 'ACC', 'ACA', 'ACG'], 'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
        'Tyr': ['TAT', 'TAC'], 'His': ['CAT', 'CAC'], 'Gln': ['CAA', 'CAG'],
        'Asn': ['AAT', 'AAC'], 'Lys': ['AAA', 'AAG'], 'Asp': ['GAT', 'GAC'],
        'Glu': ['GAA', 'GAG'], 'Cys': ['TGT', 'TGC'], 'Trp': ['TGG'],
        'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
        'STOP': ['TAA', 'TAG', 'TGA']
    }

def build_codon_to_amino_acid(codon_table):
    codon_to_amino_acid = {}
    for amino_acid, codons in codon_table.items():
        for codon in codons:
            codon_to_amino_acid[codon] = amino_acid
    return codon_to_amino_acid

def read_dna_sequence(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            if content.startswith('>'):
                return ''.join(content.split('\n')[1:]).upper()
            return content.upper()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None

def translate_dna_to_protein(dna_sequence, codon_to_amino_acid):
    protein = []
    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i + 3]
        amino_acid = codon_to_amino_acid.get(codon, 'STOP')
        if amino_acid == 'STOP':
            break
        protein.append(amino_acid)
    return protein

def count_amino_acids(protein):
    amino_acid_count = {}
    for amino_acid in protein:
        if amino_acid in amino_acid_count:
            amino_acid_count[amino_acid] += 1
        else:
            amino_acid_count[amino_acid] = 1
    return amino_acid_count

def main(file_path):
    codon_table = get_codon_table()
    codon_to_amino_acid = build_codon_to_amino_acid(codon_table)
    dna_sequence = read_dna_sequence(file_path)
    if dna_sequence is None:
        return
    protein = translate_dna_to_protein(dna_sequence, codon_to_amino_acid)
    amino_acid_count = count_amino_acids(protein)

    print("Amino Acid Counts:")
    for amino_acid, count in amino_acid_count.items():
        print(f"{amino_acid}: {count}")

if __name__ == "__main__":
    main("dna_sequence.txt")

