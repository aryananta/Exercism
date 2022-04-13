def proteins(strand):
    #pass
    
    if len(strand) % 3 != 0:
        raise Exception("cannot translate the strand")

    stop_index = 3
    protein = []
    
    new_strand = [strand[i:i+stop_index] for i in range(0,len(strand),stop_index)]
    '''
    protein name
    
    '''
    methionine = ["AUG"]
    phenylalanine = ["UUU", "UUC"]
    leucine = ["UUA", "UUG"]
    serine = ["UCU", "UCC", "UCA", "UCG"]
    tyrosine = ["UAU", "UAC"]
    cysteine = ["UGU", "UGC"]
    tryptophan = ["UGG"]
    stop_codon = ["UAA", "UAG", "UGA"]
    
    '''
    get stop codon index in strand
    '''
    
    for cod in new_strand:
        if cod in methionine:
            protein.append("Methionine")
        if cod in phenylalanine:
            protein.append("Phenylalanine")
        if cod in leucine:
            protein.append("Leucine")
        if cod in serine:
            protein.append("Serine")
        if cod in tyrosine:
            protein.append("Tyrosine")
        if cod in cysteine:
            protein.append('Cysteine')
        if cod in tryptophan:
            protein.append('Tryptophan')
        if cod in stop_codon:
            break
    
    return protein
   