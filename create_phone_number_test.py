from create_phone_number import create_phone_number

def test_create_phone_number():
    assert  create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9]) == '(123) 456-789'
    assert  create_phone_number([1, 'b', 3, 4, 5, 'a', 7, 8, 9]) == '(1b3) 45a-789'
