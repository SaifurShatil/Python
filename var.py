a=10
print(id(a))
b=a
print(id(b))
a=9
print(id(a))
print(id(b))

#define constant by capital declaration
PI=3.14
print(type(PI))

print(range(10))
print(list(range(10)))
print(list(range(10,20)))
print(list(range(2,10,2)))


a,b=5,6
print(a)

print(bin(a))
print(0b101)

print(oct(a))
print(hex(a))
print(0x5)

#swap
a=a+b
b=a-b
a=a-b
print(a,b)

#reduce xtra memory
a=a^b
b=a^b
a=a^b
print(a,b)

#2 rotation
a,b=b,a
print(a,b)
####

print(~12)
print(~65)

print(25 and 30)
print(25 & 30)
print(10<<2)

#####
from math import *
x=sqrt(34)
print(x)
print(floor(3.6))
print(ceil(3.2))

print(3**2)
print(pow(3,2))
print(pi)
print(e)

import math as m
print(m.sqrt(25))

from math import sqrt,pow
print(pow(2,6))


