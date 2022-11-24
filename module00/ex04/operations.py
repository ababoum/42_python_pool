'''
This program computes the 5 elementary math operations between the 2 inputs provided.
'''

import sys

args = sys.argv
args.pop(0)

USAGE = "usage: python3 operations.py <number1> <number2>"

if not args:
    sys.exit(USAGE)

if len(args) > 2:
    print("AssertionError: too many arguments", file=sys.stderr)
    sys.exit(USAGE)
elif len(args) < 2:
    print("AssertionError: not enough arguments", file=sys.stderr)
    sys.exit(USAGE)

try:
    NUMBER1 = int(args[0])
    NUMBER2 = int(args[1])
except ValueError:
    print("AssertionError: only integers", file=sys.stderr)
    sys.exit(USAGE)

print(f'{"Sum":12}{NUMBER1+NUMBER2}')
print(f'{"Difference:":12}{NUMBER1-NUMBER2}')
print(f'{"Product:":12}{NUMBER1*NUMBER2}')
try:
    print(f'{"Quotient:":12}{NUMBER1/NUMBER2}')
except ZeroDivisionError:
    print(f'{"Quotient:":12}{"ERROR (division by zero)"}')
try:
    print(f'{"Quotient:":12}{NUMBER1 % NUMBER2}')
except ZeroDivisionError:
    print(f'{"Quotient:":12}{"ERROR (modulo by zero)"}')
