'''
This module includes a function that analyzes the content of a text by counting
the number of uppercase letters, lowercase letters, punctation marks, spaces, and
the total number of characters.
'''

import sys
import string


def text_analyzer(text=""):
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    '''
    if text is None or not text:
        print("What is the text to analyze?")
        try:
            text = input()
        except EOFError:
            text = ""
        text_analyzer(text)
        return
    if not isinstance(text, str):
        print("AssertionError: argument is not a string", file=sys.stderr)
        return

    upper_count = 0
    lower_count = 0
    punct_count = 0
    space_count = 0
    char_count = 0

    for char in text:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
        elif char == ' ':
            space_count += 1
        elif char in string.punctuation:
            punct_count += 1
        char_count += 1
    print(f'The text contains {char_count} character(s):')
    print(f'- {upper_count} upper letter(s)')
    print(f'- {lower_count} lower letter(s)')
    print(f'- {punct_count} punctuation mark(s)')
    print(f'- {space_count} space(s)')


if __name__ == "__main__":
    arguments = list(sys.argv)
    arguments.pop(0)
    if len(arguments) > 1:
        print("AssertionError: more than one argument are provided", file=sys.stderr)
        sys.exit()
    elif not arguments:
        text_analyzer()
    else:
        text_analyzer(arguments[0])
