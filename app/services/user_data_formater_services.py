import re


def data_formater(data):
    data["email"] = data["email"].lower()

    data["cep"] = f"{data['cep'][0:5]}-{data['cep'][-3:]}"

    phone_pattern = "([0-9]{2})([0-9]{4,5})([0-9]{4})"
    formater = re.search(phone_pattern, data["phone"])
    data["phone"] = "({}){}-{}".format(
        formater.group(1), formater.group(2), formater.group(3)
    )

    return data
