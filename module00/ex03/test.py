'''
This module is an examples file to stress-test count.py
'''

from count import text_analyzer

text_analyzer("Python 2.0, released 2000, introduced features \
like List comprehensions and a garbage collection system capable \
of collecting reference cycles.")

print("===============================")

text_analyzer("Python is an interpreted, high-level, \
general-purpose programming language. Created by Guido van Rossum and first \
released in 1991, Python's design philosophy emphasizes code readability with \
its notable use of significant whitespace.")

print("===============================")

text_analyzer()

print("===============================")

text_analyzer(42)

print("===============================")

print(text_analyzer.__doc__)
