seq1 = input('Please input the DNA sequence: ')
seq2 = seq1.upper()
s = ''
for i in range(len(seq2)):
    if seq2[i] == 'A':
        s = 'T' + s
    elif seq2[i] == 'C':
        s = 'G' + s
    elif seq2[i] == 'G':
        s = 'C' + s
    elif seq2[i] == 'T':
        s = 'A' + s
    else:
        print('It is not a DNA sequence.')
        break

# make sure the input is a DNA sequence and then output the reverse complement
if len(seq2) == len(s):
    print(s)

# example: seq = 'AtGTagTGCGTcGT'
# returns 'ACGACGCACTACAT'