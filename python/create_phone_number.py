def create_phone_number(num):
    result = "".join([str(digit) for digit in num])
    return f"({result[:3]}) {result[3:6]}-{result[6:]}"
