#!/usr/bin/python3

def roman_to_int(roman_string):
    """Convert a Roman numeral to an integer.

    Args:
        roman_string (str): Roman numeral string.

    Returns:
        int: Integer value of the Roman numeral, or 0 if invalid.
    """
    if not roman_string:
        return 0

    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    total = 0
    length = len(roman_string)

    for i in range(length):
        current_value = roman_map[roman_string[i]]

        if (
            i < length - 1
            and current_value < roman_map[roman_string[i + 1]]
        ):
            total -= current_value
        else:
            total += current_value

    return total
