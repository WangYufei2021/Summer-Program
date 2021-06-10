from re import sub
codon_table = {
    'TTT': 'F', 'TCT': 'S', 'TAT': 'Y', 'TGT': 'C',
    'TTC': 'F', 'TCC': 'S', 'TAC': 'Y', 'TGC': 'C',
    'TTA': 'L', 'TCA': 'S', 'TAA': 'O', 'TGA': 'X',
    'TTG': 'L', 'TCG': 'S', 'TAG': 'U', 'TGG': 'W',
    'CTT': 'L', 'CCT': 'P', 'CAT': 'H', 'CGT': 'R',
    'CTC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
    'CTA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',
    'CTG': 'L', 'CCG': 'P', 'CAG': 'Z', 'CGG': 'R',
    'ATT': 'I', 'ACT': 'T', 'AAT': 'N', 'AGT': 'S',
    'ATC': 'I', 'ACC': 'T', 'AAC': 'B', 'AGC': 'S',
    'ATA': 'J', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
    'ATG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
    'GTT': 'V', 'GCT': 'A', 'GAT': 'D', 'GGT': 'G',
    'GTC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
    'GTA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'A',
    'GTG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'}


def transcribe(dna_seq, direction='-'):
    rna_seq = ''
    if direction == '+':
        compliment = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
        for base in dna_seq:
            rna_seq += compliment[base]
    elif direction == '-':
        rna_seq = sub('T', 'U', dna_seq)
    else:
        raise ValueError("`direction` must be either '+' or '-'.")

    return(rna_seq)


def translate(rna_seq, codon_to_amino):
    start_codon = 'AUG'
    stop_codons = ['UAA', 'UAG', 'UGA']
    aa_seq = ''
    pos = 0
    codon = rna_seq[pos:pos + 3]
    seq_length = len(rna_seq)

    while codon != start_codon and pos != seq_length - 3:
        pos += 1
        codon = rna_seq[pos:pos + 3]

    while pos < seq_length - 3 and codon not in stop_codons:
        codon = rna_seq[pos:pos + 3]
        aa_seq += codon_to_amino[codon]
        pos += 3

    if len(aa_seq) == 0:
        print('No translateable sequence found.')

    return(aa_seq)


def read_fasta(fasta_file):
    sequence = ''
    with open(fasta_file) as read_file:
        for line in read_file:
            if line[0] not in ['>', ';']:
                sequence += line.strip()
    return(sequence)


def write_fasta(sequence, output_file, desc=''):
    write_file = open(output_file, 'w')
    write_file.write('>' + desc + '\n')
    seq_length = len(sequence)

    for i in range(0, seq_length, 80):
        write_file.write(sequence[i:i + 80] + '\n')
    write_file.write(sequence[i:seq_length])
    write_file.close()


def main(dna_seq, output_fasta):
    rna_seq = transcribe(dna_seq, '-')
    codon_to_amino = codon_table
    aa_seq = translate(rna_seq, codon_to_amino)
    write_fasta(aa_seq, output_fasta)
