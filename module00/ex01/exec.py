import sys

arguments = list(sys.argv)
arguments.pop(0)

if not arguments:
    sys.exit("usage: python3 exec.py arg1 arg2 ... argn")

str = ' '.join(arguments)

str = str[::-1]
res = []

for c in str:
    if c.isupper():
        res += c.lower()
    elif c.islower():
        res += c.upper()
    else:
        res += c

print(''.join(res))
