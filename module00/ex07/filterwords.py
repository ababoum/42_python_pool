'''
This module defines a program that displays all the words in a sentence that
satisfy a minimum-length condition
'''


import sys
import string


# CHECK AND SANITIZE INPUT
args = sys.argv
args.pop(0)

if not args:
    sys.exit("ERROR")
if len(args) != 2:
    sys.exit("ERROR")

try:
    THRESHOLD = int(args[1])
except ValueError:
    sys.exit("ERROR")

listed_input = args[0].split()


# DEFINE USEFUL FUNCTIONS

def word_length(word):
    '''
    Calculates a word's length without punctuation
    '''
    count = 0
    for char in word:
        if char not in string.punctuation:
            count += 1
    return count


def trim_words(lst):
    '''
    Removes punctuation from word-strings
    '''
    new_list = []
    translation_table = dict.fromkeys(map(ord, string.punctuation), None)
    for item in lst:
        new_list.append(item.translate(translation_table))
    return new_list


# ACTUAL PROGRAM
print(
    f'{trim_words([word for word in listed_input if word_length(word) > THRESHOLD])}')
