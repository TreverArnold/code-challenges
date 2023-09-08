from break_camel_case import break_camel_case

def test_break_camel_case():
    assert break_camel_case("helloWorld") == "hello World"
    assert break_camel_case("th8Abc") == "th8 Abc"
    assert break_camel_case("camelCase") == "camel Case"
