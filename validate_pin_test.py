from validate_pin import validate_pin

def test_validate_pin():
    assert validate_pin('098765') == True
    assert validate_pin('1234') == True
    assert validate_pin('a243') == False
    assert validate_pin('34234') == False

