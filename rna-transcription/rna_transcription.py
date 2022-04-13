def to_rna(dna_strand):
    #pass
    
    if isinstance(dna_strand,str):
        rna_strand = ""
        for char in dna_strand:
            if char == "G":
                rna_strand = rna_strand + "C"
            elif char == "C":
                rna_strand = rna_strand + "G"
            elif char == "T":
                rna_strand = rna_strand + "A"
            elif char == "A":
                rna_strand = rna_strand + "U"
    
        return rna_strand
    else:
        raise Exception("Meaningful message indicating the source of the error")

