import json

# Retrieve the list of trees:
ptFile = open('C:\Python2\PA2\parse_train_rare_t.dat', 'r')
trees = []
with ptFile as l:
    for line in l:
        trees.append(json.loads(line))

ptFile.close()

# Retrieve rules with probabilities:

# Binary Rules probabilities dictionary:
prbFile = open('C:\Python2\PA2\q.bin', 'r')

brDict = {}
pstr = prbFile.readline()
while pstr != '':
    brDict[' '.join(pstr.split(' ')[:-2])] = pstr.split(' ')[-2]
    pstr = prbFile.readline()

prbFile.close()

# Unary Rules probabilities dictionary:
pruFile = open('C:\Python2\PA2\q.uni', 'r')

urDict = {}
pstr = pruFile.readline()
while pstr != '':
    urDict[' '.join(pstr.split(' ')[:-2])] = pstr.split(' ')[-2]
    pstr = pruFile.readline()

pruFile.close()


# Function that retrieve rule values:
def extract_list_values(li):
    bi = li[0] + ' ' + li[1][0] + ' ' + li[2][0]
    BinList.append(bi)
        
    for item in li:
        if len(item) == 3:
            extract_list_values(item)
        elif len(item) == 2 and isinstance(item, list):
            UniList.append(item)
                
    return BinList, UniList

# Count probability for each tree and add value to dictionary:
treepDict = {}
prb = 1
for tree in trees:
    BinList = []
    UniList = []
    extract_list_values(tree)
    for item in BinList:
        for key in brDict:
            if item == key:
                prb = prb * float(brDict[key])
    treepDict[str(tree)] = prb

for key in treepDict:
    print key
    print treepDict[key]

 
    
    

        

