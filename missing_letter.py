def missing_letter(chars):
    alphabet = "abcdefghijklmnopqrstuvwxyz"   
    
    for letter in chars: 
        index = alphabet.index(letter.lower())
        if alphabet[index + 1] not in chars and alphabet[index + 1].upper() not in chars:
            if letter.isupper():
                return alphabet[index+1].upper()
            else:
                return alphabet[index+1]

