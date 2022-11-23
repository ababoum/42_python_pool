import sys

arguments = list(sys.argv)
arguments.pop(0)

if not arguments:
    sys.exit("usage: python3 whois.py [integer]")

if len(arguments) != 1:
    print("AssertionError: more than one argument are provided", file=sys.stderr)
    sys.exit()

try:
    arg = int(arguments[0])
    if arg == 0:
        print("I'm Zero.")
    elif arg % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")
except:
    print("AssertionError: argument is not an integer", file=sys.stderr)