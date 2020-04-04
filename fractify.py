from math import gcd
#gcd = greatest common denominator

def fractify(obj):
    if (isinstance(obj,tuple) and
        len(obj)==2 and
        isinstance(obj[0], int) and
        isinstance(obj[1], int)):
        return simplify(obj)
    else:
        return (obj,1)

def simplify(f1):
    n1, d1 = f1
    _gcd = gcd(n1, d1)
    return (n1//_gcd, d1//_gcd)
# // = divisione con troncamento alla decina

def sum(f1, f2):
    n1, d1 = f1
    n2, d2 = f2
    dt = d1*d2
    nt = n1*d2+n2*d1
    return simplify((nt, dt))

def prod(f1,f2):
    n1, d1 = f1
    n2, d2 = f2
    return simplify((n1*n2, d1*d2))

f1 = (3,4)
f2 = (5,7)

def test_sum_commutative(f1, f2):
    assert sum(f1,f2) == sum(f2,f1)

def test_identity_element(f1):
    zero = (0,1)
    assert sum(f1, zero) == f1

#these are properties that I am testing i.e. property tests

print ("ciao!") -> prints to std output

import sys
print("ciao!", filesys.stderr) -> prints to std error
