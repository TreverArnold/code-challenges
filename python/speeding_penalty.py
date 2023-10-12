def penalty(numbers):
    numbers.sort(key=lambda x: x*2)
    return ''.join(numbers)