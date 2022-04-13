def convert(number):
    #pass
    feed = ''
    if number % 3 == 0:
        feed = feed + "Pling"
    if number % 5 == 0:
        feed = feed + "Plang"
    if number % 7 == 0:
        feed = feed + "Plong"
    if not feed:
        feed = str(number)
    
    return feed 
    
        
