xfile = open(input('Please input the file name: '), 'r')  # EcoliK12.fasta
sequence1 = ''
for line in xfile:
    if not line.startswith('>'):
        sequence1 = sequence1 + line.replace('\n', '')

counts1 = {}
num_kmers = len(sequence1) - 3 + 1
for i in range(num_kmers):
    kmer = sequence1[i:i + 3]
    if kmer not in counts1:
        counts1[kmer] = 0
    else:
        counts1[kmer] = counts1[kmer] + 1
print(counts1)

xfile = open(input('Please input the file name: '), 'r')  # EcoliO157.fasta
sequence2 = ''
for line in xfile:
    if not line.startswith('>'):
        sequence2 = sequence2 + line.replace('\n', '')

counts2 = {}
num_kmers = len(sequence2) - 3 + 1
for i in range(num_kmers):
    kmer = sequence2[i:i + 3]
    if kmer not in counts2:
        counts2[kmer] = 0
    else:
        counts2[kmer] = counts2[kmer] + 1
print(counts2)

s = 0
d = 0
for i in counts1:
    if i in counts2:
        d = d + (int(counts1[i]) - int(counts2[i])) ** 2
    else:
        d = d
s = d ** (1 / 2)
print('the distance is ', s)