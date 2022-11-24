'''
This program checks if an input is odd, even, or if it is equal to zero.
'''

import sys

arguments = list(sys.argv)
arguments.pop(0)

if not arguments:
    sys.exit("usage: python3 whois.py [integer]")

if len(arguments) != 1:
    print("AssertionError: more than one argument are provided", file=sys.stderr)
    sys.exit()

try:
    ARG = int(arguments[0])
    if ARG == 0:
        print("I'm Zero.")
    elif ARG % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")
except ValueError:
    print("AssertionError: argument is not an integer", file=sys.stderr)
