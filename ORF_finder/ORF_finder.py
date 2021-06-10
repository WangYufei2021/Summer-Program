xfile = open(input('Please input the file name: '), 'r')
# EcoliK12.fasta
sequence = ''
for line in xfile:
    if not line.startswith('>'):
        sequence = sequence + line.replace('\n', '')
seq = sequence


def start_codon_finder(seq):
    term = True
    while term == True:
        splice = seq[:2]
        if splice == 'ATG':
            term = False
            return seq
        seq = seq[3:]
        if len(seq) == 0:
            term = False


splice_codon = [0, 1, 2]
store_list = []
for i in splice_codon:
    temp_seq = seq[i:]
    temp = start_codon_finder(temp_seq)
    store_list.append(temp)

def stop_codon_finder(seq):
    term = True
    accumu_str = ''
    while term == True:
        splice = seq[:3]
        if splice == 'TAG' or 'TAA' or 'TGA':
            term = False
            return accumu_str
        accumu_str = accumu_str + seq[:3]
        seq = seq[3:]
        if len(seq) == 0:
            term = False


complement = ''
for i in range(len(sequence)):
    if sequence[i] == 'A':
        complement = 'T' + complement
    elif sequence[i] == 'C':
        complement = 'G' + complement
    elif sequence[i] == 'G':
        complement = 'C' + complement
    elif sequence[i] == 'T':
        complement = 'A' + complement

seq = complement

for i in splice_codon:
    temp_seq = seq[i:]
    temp = start_codon_finder(temp_seq)
    store_list.append(temp)


for i in store_list:
    temp = stop_codon_finder(i)
    if len(str(temp)) > 51:
        print(temp)