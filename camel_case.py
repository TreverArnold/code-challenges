def camel_case(s):
    result = ""
    wordarr = s.split(" ")
    for word in wordarr:
        result += word.capitalize()

    return result
