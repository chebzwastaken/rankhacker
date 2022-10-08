def timeConversion(s):
    """
    Given a time in -hour AM/PM format, convert it to military (24-hour) time.
    """

    """
    Explanation:
    1. We check if the last two characters of the string are PM.
    2. If they are, we check if the first two characters of the string are 12. If they are, we return the string 12 and the characters from index 2 to the second last character of the string.
    3. If the first two characters are not 12, we return the string representation of the integer obtained by adding 12 to the integer representation of the first two characters of the string and the characters from index 2 to the second last character of the string.
    4. If the first two characters of the string are 12 and the last two characters are AM, we return 00 and the characters from index 2 to the second last character of the string.
    5. If none of the above conditions are satisfied, we return the string from index 0 to the second last character of the string.
    """
    if s[-2:] == 'PM':
        if int(s[:2]) + 12 == 24:
            return '12' + s[2:-2]
        return str(int(s[:2]) + 12) + s[2:-2]
    elif s[:2] == '12' and s[-2:] == 'AM':
        return '00' + s[2:-2]
    return s[:-2]




print(timeConversion('12:45:54PM'))
