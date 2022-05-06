import re

from app.exceptions.data_validation_exc import InvalidFormat


def validate_data(data):

    email = data.get("email", None)
    cep = data.get("cep", None)
    phone = data.get("phone", None)

    if email:

        email = email.lower()

        email_pattern = "^[a-zA-Z0-9.!#$%&'+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)$"
        email_form = re.fullmatch(email_pattern, email)

        if not email_form:
            raise InvalidFormat("email", "name@email.com", email)

    if cep:

        cep_pattern = "[0-9]{5}-[0-9]{3}"
        cep_form = re.fullmatch(cep_pattern, cep)

        if not cep_form:
            raise InvalidFormat("cep", "xxxxx-xxx", cep)

    if phone:

        phone_pattern = "\([0-9]{2}\) [0-9]{5}-[0-9]{4}"
        phone_form = re.fullmatch(phone_pattern, phone)

        print("=" * 60)
        print()
        print(phone)
        print(phone_form)
        print()
        print("=" * 60)

        if not phone_form:
            raise InvalidFormat("phone", "(xx) xxxxx-xxxx", phone)
