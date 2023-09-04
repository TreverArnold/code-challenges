import re

def ends_with(text, ending):
    pattern = re.escape(ending) + '$'
    return bool(re.search(pattern, text))
