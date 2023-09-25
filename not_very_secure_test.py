from not_very_secure import not_very_secure


def test_not_very_secure():
    assert not_very_secure("ahIbsFiasd") == True
    assert not_very_secure("ahi0bsfi935674asd334") == True
    assert not_very_secure("ahi0bsfi9/>35674asd33?4") == False
    assert not_very_secure("ahJb  jbkjl") == False
    assert not_very_secure("ahJb__jbkjl") == False
    assert not_very_secure("") == False
