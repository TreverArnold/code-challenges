def vowel_count(string):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return(count)