print("This is a genome decoder")
print("")
# Codon to Amino Acid Mapping
codon_table = {
    'ATA':'Isoleucine', 'ATC':'Isoleucine', 'ATT':'Isoleucine', 'ATG':'Methionine',
    'ACA':'Threonine', 'ACC':'Threonine', 'ACG':'Threonine', 'ACT':'Threonine',
    'AAC':'Asparagine', 'AAT':'Asparagine', 'AAA':'Lysine', 'AAG':'Lysine',
    'AGC':'Serine', 'AGT':'Serine', 'AGA':'Arginine', 'AGG':'Arginine',                
    'CTA':'Leucine', 'CTC':'Leucine', 'CTG':'Leucine', 'CTT':'Leucine',
    'CCA':'Proline', 'CCC':'Proline', 'CCG':'Proline', 'CCT':'Proline',
    'CAC':'Histidine', 'CAT':'Histidine', 'CAA':'Glutamine', 'CAG':'Glutamine',
    'CGA':'Arginine', 'CGC':'Arginine', 'CGG':'Arginine', 'CGT':'Arginine',
    'GTA':'Valine', 'GTC':'Valine', 'GTG':'Valine', 'GTT':'Valine',
    'GCA':'Alanine', 'GCC':'Alanine', 'GCG':'Alanine', 'GCT':'Alanine',
    'GAC':'Aspartic Acid', 'GAT':'Aspartic Acid', 'GAA':'Glutamic Acid', 'GAG':'Glutamic Acid',
    'GGA':'Glycine', 'GGC':'Glycine', 'GGG':'Glycine', 'GGT':'Glycine',
    'TCA':'Serine', 'TCC':'Serine', 'TCG':'Serine', 'TCT':'Serine',
    'TTC':'Phenylalanine', 'TTT':'Phenylalanine', 'TTA':'Leucine', 'TTG':'Leucine',
    'TAC':'Tyrosine', 'TAT':'Tyrosine', 'TAA':'Stop', 'TAG':'Stop',
    'TGC':'Cysteine', 'TGT':'Cysteine', 'TGA':'Stop', 'TGG':'Tryptophan',
}

short_codon_table = {
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
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
}

# Function to convert DNA sequence into amino acids
def dna_to_amino_acids():
    print("converting")
    with open('dna.txt', 'r') as file:
        content = file.read()
        file.close()
    
    # Ensure length of sequence is divisible by 3
    if len(content) % 3 != 0:
        print(len(content))
        print(content%3)
        raise ValueError("DNA sequence length must be a multiple of 3")
    
    short_amino_acids = []
    amino_acids = []
    amino_acid_count = {}
    
    # Iterate through the sequence in steps of 3 nucleotides (codons)
    for i in range(0, len(content), 3):
        codon = content[i:i+3]  # Get a codon (3 nucleotides)
        amino_acid = codon_table.get(codon, 'Unknown')  # Get corresponding amino acid
        short_amino_acid = short_codon_table.get(codon, 'Unknown')
        amino_acids.append(amino_acid)
        short_amino_acids.append(short_amino_acid)
        
        if amino_acid in amino_acid_count:
            amino_acid_count[amino_acid] += 1
        else:
            amino_acid_count[amino_acid] = 1
    
    with open('aminoAcids_Results.txt', 'w') as file:
        file.write(''.join(short_amino_acids))
        file.write("\n")
        file.write(str(amino_acids))
        file.write("\n")
        file.write(str(amino_acid_count))
        file.close()

def compare_sequences():
    print("comparing")
    with open('dna1.txt', 'r') as file:
        content1 = file.read()
        file.close()
    
    with open('dna2.txt', 'r') as file:
        content2 = file.read()
        file.close()
    
    l1 = len(content1)
    l2 = len(content2)
    
    if l1>l2:
        l = l1-l2
        content1 = content1[:l1-l]
    elif l2>l1:
        l = l2-l1
        content2 = content2[:l2-l]
    
    similar_sequences = []
    
    x = 0
    while x < l1-3:
        if content1[x:x+3] == content2[x:x+3]:
            sub = content1[x:x+3]
            if len(sub) == 3 and sub.isalpha():  # Check if the substring is exactly 3 characters long
                similar_sequences.append(sub)
                print(sub)
        x += 3
                
    with open('comparison_Results.txt', 'w') as file:
        file.write("similarities = " + str(len(similar_sequences)))
        file.write("\n")
        for s in similar_sequences:
            file.write(s)
            file.write("\n")
        file.close()    

while True:
    print("Enter 1 if you want to convert a dna to amino acids")
    print("Enter 2 if you want to compare two dna sequences")
    opt = input()
    
    if opt == '1':
        print("When running this code make sure that a file named dna.txt exists in the same folder as this code")
        o = input("press enter when ready to run")
        dna_to_amino_acids()
    elif opt == '2':
        print("When running this code make sure that a files named dna1.txt and dna2.txt exist in the same folder as this code")
        o = input("press enter when ready to run")
        compare_sequences()
        
    print()