import re
def break_camel_case(s):
    str = ''
    s = re.split(r'(?=[A-Z])', s)
    for word in s:
        str += word + ' '
    return str.rstrip()