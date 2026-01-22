#!/usr/bin/python3

def roman_to_int(roman_string):
    
    if not roman_string or roman_string == "":
        return 0
    
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    n = len(roman_string)

    # Iterate through the string, checking the next character for subtraction cases
    for i in range(n):
        current_value = roman_map[roman_string[i]]
        
        # If not the last character and current value is less than the next
        if i < n - 1 and current_value < roman_map[roman_string[i+1]]:
            total -= current_value # Subtract (e.g., for 'I' in 'IV')
        else:
            total += current_value # Add (e.g., for 'V' in 'VI' or 'V' in 'IV')
            
    return total
