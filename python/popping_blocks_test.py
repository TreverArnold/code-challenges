from popping_blocks import pop_blocks


def test_pop_blocks():
    assert pop_blocks(['B', 'B', 'A', 'C', 'A', 'A', 'C']) == ['A']
    assert pop_blocks(['B', 'B', 'A', 'C', 'A', 'A', 'C', 'B']) == ['A', 'B']
    assert pop_blocks(['B', 'B', 'C', 'A', 'A', 'C']) == []
    assert pop_blocks([]) == []


