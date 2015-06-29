# Replaces terminal symbols in data with count less than 5

import json

# Get Word Counts:

countsFile = open('C:\Python2\PA2\cfg.counts', 'r')

cList = countsFile.readlines()

wordsD = {} # Dictionary for words to be replaced
for n in range(len(cList)):
    if cList[n].split(' ')[1] == 'UNARYRULE':
        if cList[n].split(' ')[3][:-1] in wordsD:
            wordsD[cList[n].split(' ')[3][:-1]] = str(int(wordsD[cList[n].split(' ')[3][:-1]]) + int(cList[n].split(' ')[0]))
        else:
            wordsD[cList[n].split(' ')[3][:-1]] = cList[n].split(' ')[0]

for key in list(wordsD):
    if int(wordsD[key]) >= 5:
        del wordsD[key]

countsFile.close()

# Replace words in tree

treeFile = open('C:\Python2\PA2\parse_train.dat', 'r')
new_treeFile = open('C:\Python2\PA2\parse_train_rare.dat', 'w')



'''with treeFile as f:
    for line in f:
        data.append(json.loads(line))'''

# Read the lines from the initial file and replace rare words

line = treeFile.readline()

    
while line != '':
    lineList = line.split('"')
    new_str = ''
    for item in lineList:
        if item in wordsD:
            i = lineList.index(item)
            lineList[i] = '_RARE_'
            new_str = '"'.join(lineList)
        else:
            new_str = '"'.join(lineList)
    new_treeFile.write(new_str)  
    line = treeFile.readline()


print 'Mission complete'

treeFile.close()
new_treeFile.close()
        
