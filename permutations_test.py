from permutations import permutations


def test_permutaions():
    assert permutations("a") == ["a"]
    assert all(perm in ["ab", "ba"] for perm in permutations("ab"))
    assert all(
        perm in ["abc", "acb", "cba", "cab", "bca", "bac"]
        for perm in permutations("abc")
    )
    assert all(
        perm in ["aabb", "abab", "abba", "baab", "baba", "bbaa"]
        for perm in permutations("aabb")
    )
