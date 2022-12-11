#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6,
           "VIi": 7, "VIiI": 8, "IX": 9, "X": 10, "L": 50, "XC": 90,
           "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
    romans_num = 0
    length = 0
    i = 0
    if (roman_string is None):
        return 0
    while (i < len(roman_string)):
        if (i == len(roman_string) - 1):
            romans_num += rom[roman_string[i]]
            break
        elif (rom[roman_string[i + 1]] <= rom[roman_string[i]]
              or len(roman_string) == 1):
            romans_num += rom[roman_string[i]]
        else:
            two_char_rom = roman_string[i] + roman_string[i + 1]
            romans_num += rom[two_char_rom]
            i = i + 1
        i = i + 1
    return (romans_num)
