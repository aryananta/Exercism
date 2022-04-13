def distance(strand_a, strand_b):
    # pass
    if len(strand_a) != len(strand_b):
        raise ValueError("length is not the same")
    
    # u = zip(strand_a,strand_b)
    # counter=0
    # for i,j in u:
    #     if i != j:
    #         counter += 1
        
    # return counter

    #new_list = sum([1 for i,j in zip(strand_a,strand_b) if i != j])
    new_list = sum([i!=j for i,j in zip(strand_a,strand_b)])
    return new_list
