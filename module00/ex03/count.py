import sys
import string


def text_analyzer(text=""):
    '''
    This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.
    '''
    if text == None or not text:
        print("What is the text to analyze?")
        text = input()
        text_analyzer(text)
        return
    if (type(text) != str):
        print("AssertionError: argument is not a string", file=sys.stderr)
        return

    upper_count = 0
    lower_count = 0
    punct_count = 0
    space_count = 0
    char_count = 0

    for c in text:
        if c.islower():
            lower_count += 1
        elif c.isupper():
            upper_count += 1
        elif c == ' ':
            space_count += 1
        elif c in string.punctuation:
            punct_count += 1
        char_count += 1
    print(f'The text contains {char_count} character(s):')
    print('- {} upper letter(s)'.format(upper_count))
    print('- {} lower letter(s)'.format(lower_count))
    print('- {} punctuation mark(s)'.format(punct_count))
    print('- {} space(s)'.format(space_count))


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