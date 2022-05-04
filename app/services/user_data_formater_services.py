import re

from app.exceptions.data_validation_exc import InvalidFormat


def validate_data(data):

    email_pattern = "^[a-zA-Z0-9.!#$%&'+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)$"
    email_form = re.fullmatch(email_pattern, data["email"].lower())
    
    cep_pattern = "[0-9]{5}-[0-9]{3}"
    cep_form = re.fullmatch(cep_pattern, data["cep"])

    phone_pattern = "([0-9]{2})[0-9]{5}-[0-9]{4}"
    phone_form = re.fullmatch(phone_pattern, data["phone"])
    if not email_form:    
        raise InvalidFormat('email','name@email.com',data['email'])
    if not cep_form:
        raise InvalidFormat('cep','xxxxx-xxx',data['cep'])

    if not phone_form:
        raise InvalidFormat('phone','(xx)xxxxx-xxxx',data['phone'])

