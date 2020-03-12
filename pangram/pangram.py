def is_pangram(sentence):
    if sentence == "":
        return False
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for letter in alphabet:
       if letter in sentence.lower():
           continue
       else:
           return False
    
    return True