'''
This program converts alphanumeric messages to morse code
'''

import sys


# CHECK AND SANITIZE INPUT
args = sys.argv
args.pop(0)

if not args:
    sys.exit()

SENTENCE = ' '.join(args)
SENTENCE = SENTENCE.upper()

# CHECK FOR NON-ALPHANUMERIC CHARACTERS
for c in SENTENCE:
    if not c.isalnum() and c != ' ':
        sys.exit("ERROR")

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ' ': '/'}


res = []
for c in SENTENCE:
    res.append(MORSE_CODE_DICT[c])
print(f'{" ".join(res)}')
