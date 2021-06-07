xfile = open(input('Please input the file name: '), 'r')
# EcoliK12.fasta
# EcoliO157.fasta
# caulobacterNA1000.fasta
sequence = ''
for line in xfile:
    if not line.startswith('>'):
        sequence = sequence + line.replace('\n', '')


def count_dinulc(read, k):
    counts = {}
    num_dinulc = len(read) - k + 1
    for i in range(num_dinulc):
        dinulc = read[i:i + k]
        if dinulc not in counts:
            counts[dinulc] = 0
        else:
            counts[dinulc]=counts[dinulc]+1
    print(counts)

count_dinulc(sequence, 2)