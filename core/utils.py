import re


def phone_formatting(phone):
    return re.sub(r'\D', '', phone)
