import re
def count_kmers(read, k):
    global i
    list = []
    counts = {}
    num_kmers = len(read) - k + 1
    print('k=' + str(k) + '    ' + 'number: ' + str(num_kmers) + '\n')
    for i in range(num_kmers):
        kmer = read[i:i + k]
        if kmer not in counts:
            counts[kmer] = 0
        list.append(kmer)
    nATC = 0
    nACT = 0
    nATG = 0
    nAGT = 0
    nACG = 0
    nAGC = 0
    nTAC = 0
    nTCA = 0
    nTAG = 0
    nTGA = 0
    nTCG = 0
    nTGC = 0
    nCAT = 0
    nCTA = 0
    nCAG = 0
    nCGA = 0
    nCTG = 0
    nCGT = 0
    nGAT = 0
    nGTA = 0
    nGAC = 0
    nGCA = 0
    nGCT = 0
    nGTC = 0
    for i in list:
        if i == 'ATC':
            nATC = nATC + 1
        if i == 'ACT':
            nACT = nACT + 1
        if i == 'ATG':
            nATG = nATG + 1
        if i == 'AGT':
            nAGT = nAGT + 1
        if i == 'ACG':
            nACG = nACG + 1
        if i == 'AGC':
            nAGC = nAGC + 1
        if i == 'TAC':
            nTAC = nTAC + 1
        if i == 'TCA':
            nTCA = nTCA + 1
        if i == 'TAG':
            nTAG = nTAG + 1
        if i == 'TGA':
            nTGA = nTGA + 1
        if i == 'TCG':
            nTCG = nTCG + 1
        if i == 'TGC':
            nTGC = nTGC + 1
        if i == 'CAT':
            nCAT = nCAT + 1
        if i == 'CTA':
            nCTA = nCTA + 1
        if i == 'CAG':
            nCAG = nCAG + 1
        if i == 'CGA':
            nCGA = nCGA + 1
        if i == 'CTG':
            nCTG = nCTG + 1
        if i == 'CGT':
            nCGT = nCGT + 1
        if i == 'GAT':
            nGAT = nGAT + 1
        if i == 'GTA':
            nGTA = nGTA + 1
        if i == 'GAC':
            nGAC = nGAC + 1
        if i == 'GCA':
            nGCA = nGCA + 1
        if i == 'GCT':
            nGCT = nGCT + 1
        if i == 'GTC':
            nGTC = nGTC + 1
    n = nATC+nACT+nATG+nAGT+nACG+nAGC+nTAC+nTCA+nTAG+nTGA+nTCG+nTGC+nCAT+nCTA+nCAG+nCGA+nCTG+nCGT+nGAT+nGTA+nGAC+nGCA+nGCT+nGTC
    print('ACT: ', (nACT / n) * 100, '%')
    print('ATC: ', (nATC / n) * 100, '%')
    print('ATG: ', (nATG / n) * 100, '%')
    print('AGT: ', (nAGT / n) * 100, '%')
    print('ACG: ', (nACG / n) * 100, '%')
    print('AGC: ', (nAGC / n) * 100, '%')
    print('TAC: ', (nTAC / n) * 100, '%')
    print('TCA: ', (nTCA / n) * 100, '%')
    print('TAG: ', (nTAG / n) * 100, '%')
    print('TGA: ', (nTGA / n) * 100, '%')
    print('TCG: ', (nTCG / n) * 100, '%')
    print('TGC: ', (nTGC / n) * 100, '%')
    print('CAT: ', (nCAT / n) * 100, '%')
    print('CTA: ', (nCTA / n) * 100, '%')
    print('CAG: ', (nCAG / n) * 100, '%')
    print('CGA: ', (nCGA / n) * 100, '%')
    print('CTG: ', (nCTG / n) * 100, '%')
    print('CGT: ', (nCGT / n) * 100, '%')
    print('GAT: ', (nGAT / n) * 100, '%')
    print('GTA: ', (nGTA / n) * 100, '%')
    print('GAC: ', (nGAC / n) * 100, '%')
    print('GCA: ', (nGCA / n) * 100, '%')
    print('GCT: ', (nGCT / n) * 100, '%')
    print('GTC: ', (nGTC / n) * 100, '%')
    return counts


xfile = open(input('Please input the file name: '), 'r')
# EcoliK12.fasta
# EcoliO157.fasta
# caulobacterNA1000.fasta
sequence = ''
for line in xfile:
    if not line.startswith('>'):
        sequence = sequence + line.replace('\n', '')

count_kmers(sequence, 3)