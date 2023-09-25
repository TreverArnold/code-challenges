from cakes import cakes


def test_cakes():
    assert cakes({"flour": 50, "sugar": 50}, {"flour": 500, "sugar": 500}) == 10
    assert cakes({"flour": 50, "sugar": 50}, {"flour": 5, "sugar": 5}) == 0
    assert (
        cakes({"flour": 50, "sugar": 50, "vanilla": 10}, {"flour": 55, "sugar": 55})
        == 0
    )
