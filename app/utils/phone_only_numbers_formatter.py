from re import sub


def phone_with_only_numbers(phone: str):
    formatted_phone = sub("[() -]", "", phone)
    return formatted_phone
