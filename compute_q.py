# Function to compute rule parameters.

# def compute_rp():
countsFile = open('C:\Python2\PA2\parse_train_mark.counts.out', 'r')

countsL = countsFile.readlines()

# Rule counts dictionaries
nontermD = {}
unaryD = {}
binaryD = {}
for line in countsL:
    if line.split(' ')[1] == 'NONTERMINAL':
        nontermD[line.split(' ')[2][:-1]] = line.split(' ')[0]
    elif line.split(' ')[1] == 'UNARYRULE':
        unaryD[line.split(' ')[2] + ' ' + line.split(' ')[3][:-1]] = line.split(' ')[0]
    elif line.split(' ')[1] == 'BINARYRULE':
        binaryD[line.split(' ')[2] + ' ' + line.split(' ')[3] + ' ' + line.split(' ')[4][:-1]] = line.split(' ')[0]

countsFile.close()


# Compute count parameters:


# Non-Terminal parameters:
q_bi_file = open('C:\Python2\PA2\qm.bin', 'w')

qNT = {}
for keyB in binaryD:
    for keyN in nontermD:
        if keyB.split(' ')[0] == keyN:
            qNT[keyB] =  float(binaryD[keyB])/float(nontermD[keyN])
            q_bi_file.write(keyB + ' ' + str(qNT[keyB]) + ' \n')

q_bi_file.close()

# Terminal parameters:
q_un_file = open('C:\Python2\PA2\qm.uni', 'w')

qT = {}
for keyU in unaryD:
    for keyN in nontermD:
        if keyU.split(' ')[0] == keyN:
            qT[keyU] =  float(unaryD[keyU])/float(nontermD[keyN])
            q_un_file.write(keyU + ' ' + str(qT[keyU]) + ' \n')

q_un_file.close()

print 'mission complete'
