import sys

arguments = list(sys.argv)
arguments.pop(0)
str = ' '.join(arguments)

str = str[::-1]
res = ""

for c in str:
    if c.isupper():
        res += c.lower()
    else:
        res += c.upper()

print(res)
