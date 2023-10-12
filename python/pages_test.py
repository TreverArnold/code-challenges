from pages import pages


def test_pages():
    assert pages(2, 5) == 10
    assert pages(-1, 5) == 0
