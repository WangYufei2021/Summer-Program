def count_kmers(read, k):
    counts = {}
    num_kmers = len(read) - k + 1
    for i in range(num_kmers):
        kmer = read[i:i + k]
        if kmer not in counts:
            counts[kmer] = 0
        else:
            counts[kmer] = counts[kmer] + 1
    import operator
    sorted_counts = sorted(counts.items(), key=operator.itemgetter(1))
    print(sorted_counts)


xfile = open(input('Please input the file name: '), 'r')
# EcoliK12.fasta
sequence = ''
for line in xfile:
    if not line.startswith('>'):
        sequence = sequence + line.replace('\n', '')
count_kmers(sequence, int(input('Please input the K: ')))

xfile = open(input('Please input the file name: '), 'r')
# EcoliO157.fasta
sequence = ''
for line in xfile:
    if not line.startswith('>'):
        sequence = sequence + line.replace('\n', '')
count_kmers(sequence, int(input('Please input the K: ')))

xfile = open(input('Please input the file name: '), 'r')
# caulobacterNA1000.fasta
sequence = ''
for line in xfile:
    if not line.startswith('>'):
        sequence = sequence + line.replace('\n', '')
count_kmers(sequence, int(input('Please input the K: ')))
