from itertools import combinations

def choose_best_sum(t, k, ls):
    best_sum = 0
    for combo in combinations(ls, k):
        current_sum = sum(combo)
        if current_sum <= t and current_sum > best_sum:
            best_sum = current_sum

    return best_sum if best_sum != 0 else None