def string_to_int(string):
    nums = []
    string = string.replace(" and", "")
    string = string.replace("-", " ")
    string = string.split(" ")
    specifics = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "ten": 10,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }
    for word in string:
        if word in specifics:
            nums.append(specifics[word])
        if word == "hundred":
            nums[-1] *= 100
        elif word == "thousand":
            nums = [i * 1000 for i in nums]
        elif word == "million":
            nums = [i * 1000000 for i in nums]
    return sum(nums)
