from hashtag_generator import generate_hashtag


def test_hashtag_generator():
    assert generate_hashtag("coding Is cool") == "#CodingIsCool"
    assert generate_hashtag("1h2n H Ila5") == "#1h2nHIla5"
    assert generate_hashtag("a" * 141) == False
    assert generate_hashtag("") == False
