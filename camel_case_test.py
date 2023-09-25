from camel_case import camel_case


def test_camel_case():
    assert camel_case("how are you doing") == "HowAreYouDoing"
    assert camel_case("Hello world") == "HelloWorld"
