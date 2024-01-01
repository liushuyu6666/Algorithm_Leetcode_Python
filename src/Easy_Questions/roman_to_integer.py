class Solution:
    def romanToInt(self, s: str) -> int:
        # In Roman numerals, larger values are always positioned before smaller values.
        roman_list = [
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1),
        ]

        total = 0

        for roman_s, roman_v in roman_list:
            while s.startswith(roman_s):
                total += roman_v
                s = s[len(roman_s):]

        return total



