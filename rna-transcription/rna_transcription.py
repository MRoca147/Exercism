def to_rna(dna_strand):
    translator = {"G": "C", "C": "G", "T": "A", "A": "U"}
    rna = ""
    for i in range(0, len(dna_strand)):
        for key, value in translator.items():
            if key == dna_strand[i]:
                rna += value
    return rna
