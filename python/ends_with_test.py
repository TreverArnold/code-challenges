from ends_with import ends_with


def test_ends_with():
    assert ends_with("samurai", "ai") == True
    assert ends_with("garbage", "e") == True
    assert ends_with("trash", "tr") == False
    assert ends_with("house", "us") == False
