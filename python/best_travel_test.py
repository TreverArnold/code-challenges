from best_travel import choose_best_sum


def test_best_travel():
    assert choose_best_sum(15, 3, [5, 5, 2, 4]) == 14
    assert choose_best_sum(15, 4, [5, 5, 2, 4]) == None
    assert choose_best_sum(0, 0, [0]) == None
