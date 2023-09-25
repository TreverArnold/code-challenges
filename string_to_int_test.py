from string_to_int import string_to_int


def test_string_to_int():
    assert string_to_int('one') == 1
    assert string_to_int('two') == 2
    assert string_to_int('three') == 3
    assert string_to_int('four') == 4
    assert string_to_int('five') == 5
    assert string_to_int('six') == 6
    assert string_to_int('seven') == 7
    assert string_to_int('eight') == 8
    assert string_to_int('nine') == 9
    assert string_to_int('ten') == 10
    assert string_to_int('eleven') == 11
    assert string_to_int('twelve') == 12
    assert string_to_int('thirteen') == 13
    assert string_to_int('fourteen') == 14
    assert string_to_int('fifteen') == 15
    assert string_to_int('sixteen') == 16
    assert string_to_int('seventeen') == 17
    assert string_to_int('eighteen') == 18
    assert string_to_int('nineteen') == 19
    assert string_to_int('twenty') == 20
    assert string_to_int('twenty-two') == 22
    assert string_to_int('thirty-five') == 35
    assert string_to_int('forty-six') == 46
    assert string_to_int('fifty-seven') == 57
    assert string_to_int('sixty-eight') == 68
    assert string_to_int('seventy-nine') == 79
    assert string_to_int('eighty') == 80
    assert string_to_int('ninety') == 90
    assert string_to_int('one hundred') == 100
    assert string_to_int('two hundred twenty-five') == 225
    assert string_to_int('three hundred forty-six') == 346
    assert string_to_int('four hundred fifty-nine') == 459
    assert string_to_int('five hundred') == 500
    assert string_to_int('six hundred seventy-eight') == 678
    assert string_to_int('seven hundred ninety') == 790
    assert string_to_int('eight hundred twenty-four') == 824
    assert string_to_int('nineteen hundred twenty-four') == 1924
    assert string_to_int('nine hundred ninety-nine') == 999
    assert string_to_int('one thousand') == 1000
    assert string_to_int('two thousand three hundred forty-five') == 2345
    assert string_to_int('eight thousand nine hundred ninety-nine') == 8999
    assert string_to_int('twenty three thousand four hundred fifty six') == 23456
    assert string_to_int('one million') == 1000000