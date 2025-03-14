def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """

    value = value.lower()
    value = value.replace(' ', '')
    backwrds = value[:: -1]

    if value == backwrds:
        return True
    else:
        return False
