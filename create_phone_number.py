def create_phone_number(num):
    result_str = ''.join([str(digit) for digit in num])
    return f'({result_str[:3]}) {result_str[3:6]}-{result_str[6:]}'