from itertools import zip_longest


def sum_digits(x, y, carry):
    result = int(x) + int(y)
    if carry:
        result += 1
        carry = False
    if result > 9:
        carry = True
        result -= 10
    return str(result), carry


def sum_strings(x, y):
    answer = []
    carry = False
    for a, b in zip_longest(reversed(x), reversed(y), fillvalue="0"):
        c, carry = sum_digits(a, b, carry)
        answer.append(c)
    if carry:
        answer.append("1")
    answer = "".join(reversed(answer)).lstrip("0")
    return answer if answer != "" else "0"
