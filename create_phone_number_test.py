from create_phone_number import create_phone_number

def test_create_phone_number():
    assert  create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9]) == '(123) 456-789'
    assert  create_phone_number([1, 5, 3, 1, 9, 6, 7, 2, 4, 8]) == '(153) 196-7248'
