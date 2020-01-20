"""
@author: tauamagalhaes
"""
##### Grade school multiplication algorithm

def addzero(string, zeros, left = True):
    for i in range(zeros):
        if left:
            string = '0' + string
        else:
            string = string + '0'
    return string

def gradeschoolmultiplication(x, y):
    x = str(x)
    y = str(y)
    zeropad = 0
    partialsum = 0
    for i in range(len(y) - 1, -1, -1):
        carry = 0
        partial = ''
        partial = addzero(partial, zeropad, False)
        for j in range(len(x) -1, -1, -1):
            z = int(y[i])*int(x[j])
            z += carry
            z = str(z)
            if len(z) > 1:
                carry = int(z[0])
            else:
                carry = 0
            partial = z[len(z) -1] + partial
        if carry > 0:
                partial = str(carry) + partial
        partialsum += int(partial)
        zeropad += 1
    return partialsum

gradeschoolmultiplication(1234, 5678)

##### Karatsuba Multiplication

def karatsubamultiplication(x ,y):
    x = str(x)
    y = str(y)
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    if len(x) < len(y):
        x = addzero(x, len(y) - len(x))
    elif len(y) < len(x):
        y = addzero(y, len(x) - len(y))
    n = len(x)
    j = n//2
    if (n % 2) != 0:
        j += 1    
    Bzeroadd = n - j
    Azeroadd = Bzeroadd * 2
    a = int(x[:j])
    b = int(x[j:])
    c = int(y[:j])
    d = int(y[j:])
    ac = karatsubamultiplication(a, c)
    bd = karatsubamultiplication(b, d)
    k = karatsubamultiplication(a + b, c + d)
    A = int(addzero(str(ac), Azeroadd, False))
    B = int(addzero(str(k - ac - bd), Bzeroadd, False))
    return A + B + bd

karatsubamultiplication(1234, 5678)
