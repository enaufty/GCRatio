dna_list = []

n = int(input("How many DNA strings will you use?: "))
valid_bases = ['A', 'T', 'G', 'C']

for i in range(n):
    dna_seq = input(f"{i + 1}. Enter the DNA sequence: ").upper()
    for base in dna_seq:
        if base not in valid_bases:
            print("Please enter a valid DNA sequence.")
            dna_seq = input(f"{i + 1}. Enter the DNA sequence: ").upper()
    dna_list.append(dna_seq)
def gc_content(seq):
    seq = seq.upper()
    g = seq.count('G')
    c = seq.count('C')
    total = len(seq)
    return round(((g+c)/total)*100)
for dna in dna_list:
    print(f"{dna} → GC% = {gc_content(dna)}")