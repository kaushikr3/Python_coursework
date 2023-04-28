# Homework 3
# Programming for Biologists
# Kaushik Raman

def reverse_complement(seq):
    seq_reverse = seq[::-1]
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    rev_comp = "".join(complement.get(base) for base in seq_reverse)
    return(rev_comp)


def get_orf(seq):
    
    assert len(seq)%3==0 , "Please provide a sequence with length being a multiple of three"
    seq_cap = seq.upper()
    list_seq = set(seq_cap)
    seq_set = set(["A","C","G","T"])
    assert list_seq == seq_set , "Invalid sequence, input sequence can only contain A, C, G or T"
    
    geneticcode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
    }
    
    orf1_protein = ""
    for i in range(0,len(seq),3):
      codon = seq[i:i + 3]
      orf1_protein += geneticcode[codon]
    orf1_protein = orf1_protein.split("_") 
    
    orf2_protein = ""
    for i in range(1, (len(seq)-2), 3):
        codon = seq[i:i + 3]
        orf2_protein += geneticcode[codon]        
    orf2_protein = orf2_protein.split("_")

    orf3_protein = ""
    for i in range(2, (len(seq)-1), 3):
        codon = seq[i:i + 3]
        orf3_protein += geneticcode[codon]
    orf3_protein = orf3_protein.split("_")

    orf4_protein = ""
    for i in range(0, len(seq), 3):
        codon = reverse_complement(seq)[i:i+3]
        orf4_protein += geneticcode[codon]
    orf4_protein = orf4_protein.split("_")

    orf5_protein = ""
    for i in range(1, (len(seq)-2), 3):
        codon = reverse_complement(seq)[i:i+3]
        orf5_protein += geneticcode[codon]
    orf5_protein = orf5_protein.split("_")

    orf6_protein = ""
    for i in range(2, (len(seq)-1), 3):
        codon = reverse_complement(seq)[i:i+3]
        orf6_protein += geneticcode[codon]
    orf6_protein = orf6_protein.split("_")
    
    allorfs = [{'orf1':orf1_protein,
    'orf2':orf2_protein,
    'orf3':orf3_protein,
    'orf4':orf4_protein,
    'orf5':orf5_protein,
    'orf1':orf6_protein,}]
    
    return(allorfs)