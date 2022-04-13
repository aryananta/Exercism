def distance(strand_a, strand_b):
    # pass
    if len(strand_a) != len(strand_b):
        raise ValueError("length is not the same")
    else:
        u = zip(strand_a,strand_b)
        counter=0
        for i,j in u:
            #if i==j:
            if i != j:
                counter += 1
            # else: 
            #     counter += 1
        
        return counter
