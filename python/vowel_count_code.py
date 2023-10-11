def vowel_count(string):
    vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count
