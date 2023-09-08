def create_phone_number(n):
    result_str = ''.join([str(digit) for digit in n])
    return f'({result_str[:3]}) {result_str[3:6]}-{result_str[6:]}'