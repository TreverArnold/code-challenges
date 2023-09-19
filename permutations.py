import itertools


def permutations(text):
    letter_list = [letter for letter in text]
    permutations = list(itertools.permutations(letter_list))
    unique_perms = set(permutations)
    result = []
    for perm in unique_perms:
        result.append("".join(perm))
    return result
