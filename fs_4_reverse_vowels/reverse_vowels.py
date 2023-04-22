def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    string_list = list(s)
    left = 0
    right = len(s) - 1  

    while left < right:
        if string_list[left] not in vowels:
            left += 1
        elif string_list[right] not in vowels:
            right -= 1
        else:
            string_list[left], string_list[right] = string_list[right], string_list[left]
            left += 1
            right -= 1

    return "".join(string_list)