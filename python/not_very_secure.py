import re


def not_very_secure(password):
    return bool(re.match(r"^[a-zA-Z0-9]+$", password))
