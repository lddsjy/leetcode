# if True:
#     raise TypeError
# s='AAAA'
# s.lower()
# print(chr(ord(s[0])+32)+s[1:])

# -*- coding: utf-8 -*-
# from functools import reduce
#
# def str2float(s):
#     DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     def char2num(s):
#         if s in DIGITS:
#             return DIGITS[s]
#     l = list(map(char2num,s))
#     print(l.index(None))
#     print(l)
#
#     return reduce(lambda x,y:x*10+y,l)
# print('str2float(\'123.456\') =', str2float('123.456'))
import time
def is_prime(n):
    if n<2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
        return True

t1 = time.time()
for i in range(2,10000):
    if is_prime(i):
        print(i)
t2 = time.time()
print(t2-t1)