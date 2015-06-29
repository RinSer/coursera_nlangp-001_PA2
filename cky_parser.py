import json
import operator


# CKY algorithm parser


# Extract sentences to be parsed from file

sentenceFile = open('C:\Python2\PA2\parse_test.dat', 'r')

sentenceList = []
sentence = sentenceFile.readline()
while sentence != '':
    sentenceList.append(sentence.split(' '))
    sentence = sentenceFile.readline()

# Cut off '\n'
for sentence in sentenceList:
    n = len(sentence)
    sentence[n-1] = sentence[n-1][:-1]

sentenceFile.close()


# Extract grammar with probabilities from files

biFile = open('C:\Python2\PA2\qm.bin', 'r')
unFile = open('C:\Python2\PA2\qm.uni', 'r')


# Retrieve non-terminal rules into dictionary
biDict = {}
biLine = biFile.readline()
while biLine != '':
    if not (biLine.split(' ')[1], biLine.split(' ')[2]) in biDict:
        biDict[biLine.split(' ')[1], biLine.split(' ')[2]] = [[biLine.split(' ')[0], biLine.split(' ')[3]]]
        biLine = biFile.readline()
    else:
        biDict[biLine.split(' ')[1], biLine.split(' ')[2]].append([biLine.split(' ')[0], biLine.split(' ')[3]])
        biLine = biFile.readline()

biFile.close()


# Retrieve terminal rules into dictionary
unDict = {}
unLine = unFile.readline()
while unLine != '':
    if not unLine.split(' ')[1] in unDict:
        D = {}
        D[unLine.split(' ')[0]] = unLine.split(' ')[2]
        unDict[unLine.split(' ')[1]] = (D)
        unLine = unFile.readline()
    else:
        D = {}
        D[unLine.split(' ')[0]] = unLine.split(' ')[2]
        unDict[unLine.split(' ')[1]].update(D)
        unLine = unFile.readline()

unFile.close()



# CKY Parsing algorithm


# Probabilistic CKY:
def pcky(sentence):
    n = len(sentence)
    Parse = [[i for i in range(n+1)] for j in range(n+1)] # Create Parse Matrix
    # Add unary rules:
    for w in range(n):
        for key in unDict:
            for un in unDict[key]:
                if sentence[w] == key:
                    if Parse[w][w+1] == w+1:
                        Parse[w][w+1] = [[un, key, unDict[key][un]]]
                    else:
                        Parse[w][w+1].append([un, key, unDict[key][un]])
        if not sentence[w] in unDict:
            for unR in unDict['_RARE_']:
                if Parse[w][w+1] == w+1:
                    Parse[w][w+1] = [[unR, sentence[w], unDict['_RARE_'][unR]]]
                else:
                    Parse[w][w+1].append([unR, sentence[w], unDict['_RARE_'][unR]])
        # Add binary rules:
    for span in range(2, n+1):
        for start in range(n+1-span):
            end = start + span
            for mid in range(start+1, end):
                if isinstance(Parse[start][mid], list) and isinstance(Parse[mid][end], list):
                    for X in Parse[start][mid]:
                        for Y in Parse[mid][end]:
                            if (X[0], Y[0]) in biDict:
                                for item in biDict[X[0], Y[0]]:
                                    Z = item[0]
                                    pX = float(X[-1])
                                    pY = float(Y[-1])
                                    pZ = float(item[1]) * pX * pY
                                    nl = [Z, X[:-1], Y[:-1], pZ]
                                    if isinstance(Parse[start][end], int):
                                        Parse[start][end] = [nl]
                                    elif isinstance(Parse[start][end], list):
                                        if not any(Z in li for li in Parse[start][end]):
                                            Parse[start][end].append(nl)
                                        else:
                                            for li in Parse[start][end]:
                                                if Z in li:
                                                    pr = float(li[3])
                                                    p = max(pZ, pr)
                                                    if p == pZ:
                                                        Parse[start][end].remove(li)
                                                        Parse[start][end].append(nl)
                                                        

                                                                                                        
    return Parse

# Write trees into json file:

outFile = open('C:\Python2\PA2\parse_test.p3.out', 'w') # Open output file

for s in sentenceList:
    Parse = pcky(s)
    if s[len(s)-1] == '?':
        for item in Parse[0][len(s)]:
            if item[0] == 'SBARQ':
                tree = item[:-1]
                # Write into file:
                outFile.write(json.dumps(tree)+'\n')
    else:
        for item in Parse[0][len(s)]:
            if item[0] == 'S':
                tree = item[:-1]
                # Write into file:
                outFile.write(json.dumps(tree)+'\n')


outFile.close()


print 'Mission complete'
                    
   
        
    
