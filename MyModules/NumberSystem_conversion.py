def decimal_to_binary(n):
    l = ''
    while n != 0:
        i = n // 2
        if n % 2 == 0:
            l += ('0')
        else:
            l += ('1')
        n = i
    return l[::-1]

def binary_to_decimal(n):
    n = n[::-1]
    l = 0
    for e, i in enumerate(n):
        l += int(i) * (2**e)
    return l
#############################

def decimal_to_octal(n):
    l = ''
    while n != 0:
        i = n // 8
        r = n % 8
        l += str(r)
        n = i
    return l[::-1]

def octal_to_decimal(n):
    n = n[::-1]
    l = 0
    for e, i in enumerate(n):
        l += int(i) * (8**e)
    return l
#############################

def decimal_to_hexadecimal(n):
    l = ''
    d = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    while n != 0:
        i = n // 16
        r = n % 16
        if r > 9:
            l += d[r]
        else:
            l += str(r)   
        n = i
    return l[::-1]

def hexadecimal_to_decimal(n):
    n =  n[::-1]
    d = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    l = 0
    for e, i in enumerate(n):
        if i in d:
            i = d[i]
        l += int(i) * (16**e)
    return l
################################
