import re

def vowel_count(string):
    return len(re.findall(r'[aeiouAEIOU]', string))