def is_isogram(string):
    # pass
    
    new_string = ''.join(e for e in string if e.isalpha()).lower()
    for char in new_string:
        if new_string.count(char) > 1:
            return False
    return True
