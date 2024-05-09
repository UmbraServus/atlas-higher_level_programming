#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [numerals[x] for x in roman_string]
    result = 0
    for y in range(len(numbers) - 1):
        if numbers[y] >= numbers[y + 1]:
            result += numbers[y]
        else:
            result -= numbers[y]
    return result + numbers[-1]