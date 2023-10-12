from speeding_penalty import penalty

def test_penalty():
    assert penalty(['45', '30', '50', '1']) == '1304550'
    assert penalty(['100', '10', '1']) == '100101'
    assert penalty(['32', '3']) == '323'
    assert penalty(['70', '46', '4', '19']) == '1944670'