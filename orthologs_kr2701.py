import sys
from Bio.Blast import NCBIXML

inputfile1 = NCBIXML.read(open(sys.argv[0],'r')) #read file1 from CLI
inputfile2 = NCBIXML.read(open(sys.argv[1],'r')) #read file2 from CLI
output = open(sys.argv[2],'w') # read output file to be written


E_VALUE_THRESH=1e-20

protein1  = []
for alignment in inputfile1.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            protein1.apprend('ProtienID:', alignment.title)
            #print('e value:', hsp.expect)
            
protein2 = []
for alignment in inputfile2.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            protein2.append('ProtienID:', alignment.title)
            #print('e value:', hsp.expect)

orthopair = []
for line1 in range(0,len(protein1)):
    for line2 in range(0,len(protein2)):
        if protein1[line1] == protein2[line2]:
            orthopair.append([protein1[line1],protein2[line2]])
output.write(orthopair)