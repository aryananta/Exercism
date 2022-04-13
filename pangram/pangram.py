import string

def is_pangram(sentence):
    #pass
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in sentence.lower():
            return False
        
    return True
