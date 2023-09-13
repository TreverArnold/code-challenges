import re

def pig_it(text):
    words = text.split(' ')
    result = []

    for word in words:
        if re.match('^[A-Za-z]+$', word):
            result.append(word[1:] + word[0] + 'ay')
        else:
            result.append(word)

    return ' '.join(result)
