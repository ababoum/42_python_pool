import sys

args = sys.argv
args.pop(0)

if not args:
    sys.exit("usage: python3 operations.py <number1> <number2>")

if len(args) > 2:
    print("AssertionError: too many arguments", file=sys.stderr)
    sys.exit()
elif len(args) < 2:
    print("AssertionError: not enough arguments", file=sys.stderr)
    sys.exit()

try:
    n1 = int(args[0])
    n2 = int(args[1])
except:
    print("AssertionError: only integers", file=sys.stderr)
    sys.exit()

print("{:12}{}".format("Sum:", n1+n2))
print("{:12}{}".format("Difference:", n1-n2))
print("{:12}{}".format("Product:", n1*n2))
try:
    print("{:12}{}".format("Quotient:", n1/n2))
except:
	print("{:12}{}".format("Quotient:", "ERROR (division by zero)"))
try:
    print("{:12}{}".format("Quotient:", n1%n2))
except:
	print("{:12}{}".format("Quotient:", "ERROR (modulo by zero)"))
