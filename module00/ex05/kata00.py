'''
Kata number 00
'''

KATA = (19, 42, 21)

print(f"The 3 numbers are: {(repr(KATA)[1:-1], repr(KATA)[1:-2])[len(KATA) == 1]}")

KATA = ()

print(f"The numbers are: {(repr(KATA)[1:-1], repr(KATA)[1:-2])[len(KATA) == 1]}")

KATA = (1, 2, 3, 5, 9, 10)

print(f"The numbers are: {(repr(KATA)[1:-1], repr(KATA)[1:-2])[len(KATA) == 1]}")

KATA = (42,)

print(f"The numbers are: {(repr(KATA)[1:-1], repr(KATA)[1:-2])[len(KATA) == 1]}")
