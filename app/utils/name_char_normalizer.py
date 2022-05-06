import re


def name_char_normalizer(name):
    """
    This function normalize the name to lowercase and remove all latin characters
    """

    latin_characters = {
        "Ááâàã": "a",
        "Ééêè": "e",
        "Ííîì": "i",
        "Óóôò": "o",
        "Úúûù": "u",
        "Çç": "c",
    }

    if type(name) == str:
        lowercase_name = name.lower()

        for char in lowercase_name:
            for key in latin_characters.keys():
                if char in key:
                    lowercase_name = re.sub(char, latin_characters[key], lowercase_name)

        return lowercase_name
