import numpy
import random
import string

def generate_password(
    password_length: int = 8,
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
        raise UserWarning("Both ignored_chars and allowed_chars have been passed!")

    if allowed_chars:
        alphabet = allowed_chars
    else:
        alphabet = list(string.ascii_lowercase)

        if has_symbols:
            alphabet.extend(["#", "!", "@"])
        if has_uppercase:
            alphabet.extend(string.ascii_uppercase)

    for ignored_char in ignored_chars:
        alphabet.remove(ignored_char)

    output = [random.choice(alphabet) for i in range(password_length)]

    if has_symbols and ["#", "!", "@"] not in output:
        output[-1] = random.choice(["#", "!", "@"])
    
    if has_uppercase and string.ascii_uppercase not in output:
        output[-2] = random.choice(string.ascii_uppercase)

    return "".join(output)
