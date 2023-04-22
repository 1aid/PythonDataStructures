def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    cap = phrase[0].upper()  # Get the first character of the string and capitalize it
    return cap + phrase[1:]
