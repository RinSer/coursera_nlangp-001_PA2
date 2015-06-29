# Replaces terminal symbols in data with count less than 5

import json

# Get Word Counts:

countsFile = open('C:\Python2\PA2\cfg_mark.counts', 'r')

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


# Function that replaces tree values:
def extract_list_values(li):
    
    for item in li:
        if len(item) == 3:
            extract_list_values(item)
        elif len(item) == 2 and isinstance(item, list):
            for key in wordsD:
                if item[1] == key:
                    item[1] = '_RARE_'
                
    return li

# Replace words in tree

treeFile = open('C:\Python2\PA2\parse_train_vert.dat', 'r')
new_treeFile = open('C:\Python2\PA2\parse_train_mark.counts.out', 'w')

with treeFile as f:
    for line in f:
        ptree = json.loads(line)
        extract_list_values(ptree)
        new_treeFile.write(json.dumps(ptree)+'\n')

treeFile.close()
new_treeFile.close()

print 'Mission complete'
        

