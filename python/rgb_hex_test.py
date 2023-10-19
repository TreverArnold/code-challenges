from rgb_hex import rgb


def test_rgb_hex():
    assert rgb(254, 253, 252) == 'FEFDFC'
    assert rgb(-20, 275, 125) == '00FF7D'
    assert rgb(1, 2, 3) == '010203'