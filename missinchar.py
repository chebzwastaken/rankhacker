import string
def missingCharaters(s):
    x = '0123456789' + string.ascii_lowercase
    y = ''
    for i in x:
        if bool(i in s) == False:
            y += i
    return y


print(missingCharaters('7985interdisciplinary12'))
