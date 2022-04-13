def classify(number):
    #pass
    if number <= 0:
        raise ValueError("should be a + number")
    divisor = [index for index in range(1,number) if number%index == 0]
    
    aliquot_sum = 0 
    
    for div in divisor:
        aliquot_sum += div
    
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"    

 