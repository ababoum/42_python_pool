'''
This programs reverses a string and reverses the characters' case
'''
import sys

arguments = list(sys.argv)
arguments.pop(0)

if not arguments:
    sys.exit("usage: python3 exec.py arg1 arg2 ... argn")

INPUT_STRING = ' '.join(arguments)

INPUT_STRING = INPUT_STRING[::-1]
res = []

for c in INPUT_STRING:
    if c.isupper():
        res += c.lower()
    elif c.islower():
        res += c.upper()
    else:
        res += c

print(''.join(res))
