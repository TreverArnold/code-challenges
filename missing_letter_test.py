from missing_letter import missing_letter

def test_missing_letter():
    assert missing_letter(['a','b','c','d','f']) == 'e'
    assert missing_letter(['O','Q','R','S']) == 'P'
