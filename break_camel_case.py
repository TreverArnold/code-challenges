import re
def break_camel_case(camel):
    result = ''
    camel = re.split(r'(?=[A-Z])', camel)
    for word in camel:
        result += word + ' '
    return result.rstrip()