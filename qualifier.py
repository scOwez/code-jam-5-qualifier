import random
import re

def generate_password(
    password_length: int = 1000000,
    has_symbols: bool = False,
    has_uppercase: bool = False,
    ignored_chars: list = [],
    allowed_chars: list = []
) -> str:
    """Generates a random password.
    The password will be exactly `password_length` characters.
    If `has_symbols` is True, the password will contain at least one symbol, such as #, !, or @.
    If `has_uppercase` is True, the password will contain at least one upper case letter.
    If `ignored_chars` is not None, characters on this list will be blacklisted
    If `allowed_chars` is not None, only characters on this list will be used
    If `ignored_chars` and `allowed_chars` are not None, `UserWarn()` will be raised
    """

    if ignored_chars and allowed_chars:
        raise UserWarning("Both ignored_chars & allowed_chars have been passed! Only 1 of these args are allowed.")

    word_dict = "abcdefghijklmnopqrstuvwxyz"
    symbols = "#!@"
    
    if has_uppercase:
        word_dict += word_dict.upper()
    elif has_symbols:
        word_dict += symbols

    output = ""

    for i in range(password_length):
        choice = random.choice(word_dict)

        if allowed_chars:
            while choice in ignored_chars or choice not in allowed_chars:
                choice = random.choice(word_dict)
        else:
            while choice in ignored_chars:
                choice = random.choice(word_dict)

        output += choice

    has_symbol = False
    has_upper = False

    for i in symbols:
        if i in output:
            has_symbol = True
            break
        elif i in word_dict.upper():
            has_upper = True
            break

    if not has_symbol:
        output = f"{output[:-1]}{random.choice(symbols)}"
    elif not has_upper:
        output = f"{output[:-2]}{random.choice(symbols)}{output[:-1]}"

    return output
