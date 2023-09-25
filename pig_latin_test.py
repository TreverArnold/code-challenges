from pig_latin import pig_it


def test_pig_it():
    assert pig_it("hello world") == "ellohay orldway"
    assert pig_it("hello 3 world i !") == "ellohay 3 orldway iay !"
