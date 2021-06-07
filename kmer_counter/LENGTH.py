xfile = open(input('Please input the file name: '), 'r')
# EcoliK12.fasta
# EcoliO157.fasta
# caulobacterNA1000.fasta
sequence =''
for line in xfile:
    if not line.startswith('>'):
        sequence = sequence+line.replace('\n', '')
print('LENGTH: ',len(sequence))