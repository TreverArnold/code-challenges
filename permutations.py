import itertools


def permutations(text):
    if len(text) == 1:
        return [text]

    letter_list = [letter for letter in text]
    return list({"".join(perm) for perm in itertools.permutations(letter_list)})
