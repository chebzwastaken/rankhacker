def timeConversion(s):
    if s[-2:] == 'PM':
        if int(s[:2]) + 12 == 24:
            return '12' + s[2:-2]
        return str(int(s[:2]) + 12) + s[2:-2]
    elif s[:2] == '12' and s[-2:] == 'AM':
        return '00' + s[2:-2]
    return s[:-2]


print(timeConversion('12:45:54PM'))
